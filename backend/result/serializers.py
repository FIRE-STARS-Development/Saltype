from rest_framework import serializers
from .models import Score,User

class ScoreSerializer(serializers.ModelSerializer):
    """
    スコアシリアライザー

    Atributes:
        user_id,score,lang_id,diff_idのバリデーション
    """
    class Meta:
        model = Score
        fields = ['user', 'score', 'lang', 'diff']
