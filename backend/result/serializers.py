from rest_framework import serializers
from .models import t_score

class ResultSerializer(serializers.ModelSerializer):
    """
    スコア結果シリアライザー

    Atributes:
        score_id、user_id、score、lang_id、diff_idをバリデーション
    """
    class Meta:
        model = t_score
        fields = ['score_id', 'user_id', 'score', 'lang_id', 'diff_id']