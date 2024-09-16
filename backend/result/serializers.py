from rest_framework import serializers
from .models import Score, User, Lang, Diff

class ScoreSerializer(serializers.ModelSerializer):
    """
    Scoreモデルのシリアライザークラス
    """
    
    """外部キーとして受け取るフィールド"""
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    lang = serializers.PrimaryKeyRelatedField(queryset=Lang.objects.all())
    diff = serializers.PrimaryKeyRelatedField(queryset=Diff.objects.all())

    class Meta:
        model = Score
        """シリアライズするフィールドを指定"""
        fields = ['user', 'score', 'lang', 'diff']

    def create(self, validated_data):
        """
        シリアライズされたデータからScoreインスタンスを作成する
        :param validated_data: バリデーション済みのデータ
        :return: 新しく作成されたScoreインスタンス
        """
        
        """バリデーション済みのデータから各フィールド取り出し"""
        user = validated_data.pop('user')
        lang = validated_data.pop('lang')
        diff = validated_data.pop('diff')
        
        """新しいScoreインスタンスを作成して保存"""
        return Score.objects.create(user=user, lang=lang, diff=diff, **validated_data)
