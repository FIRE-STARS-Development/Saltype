from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import ScoreSerializer
from .models import Rank ,User
from .utils import ScoreService

class AddScoreAndRankView(APIView):
    """
    スコアインサートとランクインサート処理

    Attributes:
        1.最高スコア判定
        2.スコアインサート
        3.ランク判定
        4.最高スコアの時のみランクインサート
    """

    """ アクセス認証（全員） """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ScoreSerializer(data=request.data)
        
        if serializer.is_valid():
            """ データ取得 """
            data = serializer.validated_data
            user_id = data.get('user_id')
            lang_id = data.get('lang_id')
            diff_id = data.get('diff_id')
            score = data.get('score')

            """ スコア判定と処理 """
            score_instance, is_high_score, new_highest_score, rank = self.process_score_and_rank(user_id, lang_id, diff_id, score, serializer)

            return Response({
                'score': ScoreSerializer(score_instance).data,
                'is_high_score': is_high_score,
                'highest_score': new_highest_score,
                'rank': rank.rank_id if rank else None,
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def process_score_and_rank(self, user_id, lang_id, diff_id, score, serializer):
        """
        スコアの挿入とランク判定、最高スコア更新の処理
        """
        """ ScoreService 初期化 """
        score_service = ScoreService(user_id, lang_id, diff_id, score)

        """ 最高スコア判定 """
        is_high_score, new_highest_score = score_service.is_new_high_score()

        """ スコアインサート """
        score_instance = serializer.save()

        """ ランク判定 """
        rank_id = score_service.determine_rank()
        rank = Rank.objects.filter(rank_id=rank_id).first()

        """ 最高スコアの場合のみユーザのランク更新 """
        if is_high_score and rank:
            user = self.update_user_rank(user_id, rank.rank_id)

        return score_instance, is_high_score, new_highest_score, rank

    def update_user_rank(self, user_id, rank_id):
        """
        ユーザのランク更新
        """
        try:
            user = User.objects.get(user_id=user_id)
            user.rank_id = rank_id
            user.save()
            return user
        except User.DoesNotExist:
            """ ユーザーが存在しない場合 """
            pass



