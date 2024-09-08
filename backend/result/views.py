# views.py
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Rank, t_score
from .serializers import ResultSerializer

@api_view(['POST'])
def add_score_and_rank(request):
    """
    スコアインサートとランク判定処理
    :param: request
    :return: 
        score: スコア
        is_high_score: 最高スコアフラグ
        rank: ランク名
    """
    serializer = ResultSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        user_id = data.get('user_id')
        lang_id = data.get('lang_id')
        diff_id = data.get('diff_id')
        score = data.get('score')

        """ 最高スコア判定 """
        is_high_score, highest_score = is_new_high_score(user_id, lang_id, diff_id, score)

        """ スコアインサート処理 """
        score_instance = t_score.objects.create(
            user_id=user_id,
            score=score,
            lang_id=lang_id,
            diff_id=diff_id
        )

        """ ランク判定処理 """
        rank_name = determine_rank(score)

        if is_high_score:
            """ 最高スコアの場合、ランクをアップデート """
            rank, created = Rank.objects.get_or_create(rank=rank_name)
        else:
            rank = Rank.objects.filter(rank=rank_name).first()

        return Response({
            'score': ResultSerializer(score_instance).data,
            'is_high_score': is_high_score,
            'rank': rank_name
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_user_rank(request):
    """
    ユーザーのランキング取得処理
    :param: request
    :return: ユーザーのランキング
    """
    user_id = request.data.get('user_id')
    lang_id = request.data.get('lang_id')
    diff_id = request.data.get('diff_id')

    if not user_id or not lang_id or not diff_id:
        return Response({"error": "Missing required parameters"}, status=status.HTTP_400_BAD_REQUEST)

    """ 指定の言語と難易度に対するスコアを降順で取得し、ユーザーの順位を取得 """
    scores = t_score.objects.filter(lang_id=lang_id, diff_id=diff_id).order_by('-score')
    
    ranking = 1
    for score_instance in scores:
        if score_instance.user_id == user_id:
            return Response({"user_rank": ranking}, status=status.HTTP_200_OK)
        ranking += 1

    """ ランキングが見つからない場合 """
    return Response({"error": "User not found in ranking"}, status=status.HTTP_404_NOT_FOUND)


def determine_rank(score):
    """
    ランク判定処理

    Attributes:
        スコアに応じてランク名をリターンする
        TODO 後々変更
    """
    if score >= 1000:
        return "係長"
    elif score >= 500:
        return "部長"
    elif score >= 100:
        return "上長"
    else:
        return "メンバー"

def is_new_high_score(user_id, lang_id, diff_id, score):
    """
    最高スコア判定処理
    
    Attributes:
        取得したスコアが最高スコアがどうか判断する
    :param 
        user_id: ユーザーID
        lang_id: 言語ID
        diff_id: 難易度ID
        score: 現在のスコア
    :return: 
        is_high_score:最高スコアフラグ
        highest_score:最高スコア
    :rtype: 
        bool
        int
    """

    """  最高スコアを取得（降順で並べて１番目のレコードを取得）"""
    highest_score = t_score.objects.filter(
        user_id=user_id,
        lang_id=lang_id,
        diff_id=diff_id
    ).order_by('-score').first()

    """ スコアが最高スコアかどうか判定 """
    if highest_score is None or score > highest_score.score:
        return True, None
    else:
        return False, highest_score

def get_or_create_rank(rank_name):
    """
    ランクアップデート処理

    Attributes:
        ランク名に一致するレコードを取得または新しく作成する
    :return: ランク名
    :rtype: str
    """
    rank, created = Rank.objects.get_or_create(rank=rank_name)
    return rank