from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .services import ScoreService
from .models import Rank, User
from .serializers import ScoreSerializer

class AddScoreAndRankView(APIView):
    """
    スコアインサートとランクインサート処理

    Attributes:
        1.最高スコア判定
        2.スコアインサート
        3.ランク判定
        4.最高スコアの時のみランクインサート
        5.ユーザのランキング取得
    """

    """ アクセス認証（全員） """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        postでリクエストが来た時の処理
        
        :return:
            score(int):スコア
            is_high_score(bool):最高スコアかどうか
            highest_score(int):最高スコア
            rank(int):ランク名
            ranking_position(int):ユーザのランキング 
        """
        serializer = ScoreSerializer(data=request.data)
        """ バリデーション通過できたら """
        if serializer.is_valid():
            """ データ取得 """
            data = serializer.validated_data
            user = data.get('user')
            lang = data.get('lang')
            diff = data.get('diff')

            """ NULLチェック """
            if not user or not lang or not diff:
                return Response({'error': 'Invalid data: user, lang or diff is None'}, status=status.HTTP_400_BAD_REQUEST)
            
            """ モデルの属性アクセス """
            user_id = user.user_id
            lang_id = lang.lang_id
            diff_id = diff.diff_id
            score = data.get('score')

            """ スコア判定と処理 """
            score_service = ScoreService(user_id, lang_id, diff_id, score)
            score_instance, is_high_score, new_highest_score, rank = self.process_score_and_rank(score_service, serializer)

            """ 現在のランキング順位取得 """
            ranking_position = score_service.get_ranking_position()

            return Response({
                'score': ScoreSerializer(score_instance).data,
                'is_high_score': is_high_score,
                'highest_score': new_highest_score,
                'rank': rank.rank_id if rank else None,
                'ranking_position': ranking_position,
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def process_score_and_rank(self, score_service, serializer):
        """
        1.最高スコア判定
        2.スコアのインサート
        3.ランク判定
        4.最高スコアの場合、最高ランクアップデート
        """
        """ 最高スコア判定 """
        is_high_score, new_highest_score = score_service.is_new_high_score()

        """ スコアインサート """
        try:
            score_instance = serializer.save()
        except Exception as e:
            print(f"Error saving score: {e}")
            return score_instance, is_high_score, new_highest_score, None

        """ ランク判定 """
        rank_id = score_service.determine_rank()
        rank = Rank.objects.filter(rank_id=rank_id).first()

        """ 最高スコアの場合のみユーザのランクアップデート """
        if is_high_score and rank:
            user = self.update_user_rank(score_service.user_id, rank.rank_id)
            if not user:
                return score_instance, is_high_score, new_highest_score, None

        return score_instance, is_high_score, new_highest_score, rank

    def update_user_rank(self, user_id, rank_id):
        """
        4.ランクアップデート処理
        """
        try:
            user = User.objects.get(user_id=user_id)
            user.rank_id = rank_id
            user.save()
            return user
        except User.DoesNotExist:
            return None