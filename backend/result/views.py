# views.py
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Rank, t_score
from .serializers import ResultSerializer
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse

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

# def get_last_30_scores(user_id, lang_id=None, diff_id=None):
#     """
#     ユーザーの過去30回のスコアを取得する
#     :param user_id: ユーザーID
#     :param lang_id: (オプション) 言語ID
#     :param diff_id: (オプション) 難易度ID
#     :return: 過去30回のスコアリスト
#     """
#     query = t_score.objects.filter(user_id=user_id).order_by('-created_at')[:30]
    
#     if lang_id:
#         query = query.filter(lang_id=lang_id)
#     if diff_id:
#         query = query.filter(diff_id=diff_id)

#     return query.values('score', 'created_at')

# def calculate_growth_rate(scores):
#     """
#     スコアの成長率を計算する
#     :param scores: ユーザーのスコアリスト
#     :return: 成長率リスト
#     """
#     growth_rates = []
#     for i in range(1, len(scores)):
#         prev_score = scores[i - 1]['score']
#         current_score = scores[i]['score']
#         growth_rate = (current_score - prev_score) / prev_score if prev_score else 0
#         growth_rates.append(growth_rate)
    
#     return growth_rates

# def plot_scores_graph(scores, growth_rates):
#     """
#     スコアのグラフを作成する
#     :param scores: スコアリスト
#     :param growth_rates: 成長率リスト
#     :return: グラフ画像
#     """
#     fig, ax1 = plt.subplots()

#     # スコアをプロット
#     ax1.set_xlabel('Attempts')
#     ax1.set_ylabel('Scores', color='tab:blue')
#     ax1.plot(range(1, len(scores) + 1), [score['score'] for score in scores], color='tab:blue', label='Scores')

#     # 成長率を別のy軸にプロット
#     ax2 = ax1.twinx()
#     ax2.set_ylabel('Growth Rate', color='tab:green')
#     ax2.plot(range(2, len(scores) + 1), growth_rates, color='tab:green', label='Growth Rate')

#     # グラフの保存
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     buf.seek(0)
#     return HttpResponse(buf.getvalue(), content_type='image/png')

# @api_view(['GET'])
# def get_growth_graph(request):
#     """
#     成長率グラフの取得
#     :param request: ユーザーID、オプションで言語IDと難易度ID
#     :return: 成長率グラフ
#     """
#     user_id = request.GET.get('user_id')
#     lang_id = request.GET.get('lang_id', None)
#     diff_id = request.GET.get('diff_id', None)

#     if not user_id:
#         return error_response({"error": "Missing user_id"})

#     # スコア取得
#     scores = get_last_30_scores(user_id, lang_id, diff_id)
    
#     if len(scores) < 2:
#         return error_response({"error": "Not enough scores for graph"})

#     # 成長率計算
#     growth_rates = calculate_growth_rate(scores)

#     # グラフを生成
#     return plot_scores_graph(scores, growth_rates)


# def error_response(errors):
#     """
#     エラーレスポンスを返す共通関数
#     :param errors: エラー内容
#     :return: Responseオブジェクト
#     """
#     return Response(errors, status=status.HTTP_400_BAD_REQUEST)