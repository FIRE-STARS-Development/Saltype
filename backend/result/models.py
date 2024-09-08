from django.db import models

    
class m_lang(models.Model):
    """
    言語マスタテーブル定義

    Attributes:
        lang_id (AutoField): 言語ID
        lang (CharField): 言語名
        created_at (DateTimeField): 作成日時
        updated_at (DateTimeField): 更新日時
        del_flg (BooleanField): 削除フラグ
    
    :return: 言語
    :rtype: str
    """
    lang_id=models.AutoField(primary_key=True)
    lang=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.lang

class m_diff(models.Model):
    """
    難易度マスタテーブル定義

    Attributes:
        diff_id (AutoField): 難易度ID。
        diff (CharField): 難易度
        created_at (DateTimeField): 作成日時
        updated_at (DateTimeField): 更新日時
        del_flg (BooleanField): 削除フラグ
    
    :return: 難易度
    :rtype: str
    """
    diff_id=models.AutoField(primary_key=True)
    diff=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.diff

class t_score(models.Model):
    """
    スコアテーブル定義

    Attributes:
        score_id (AutoField): スコアID
        user_id (ForeignKey): スコアを記録したユーザーID（CustomUserモデルへの外部キー）
        score (IntegerField): ゲームのスコア（デフォルトで0）
        lang_id (ForeignKey): 言語設定（m_langモデルへの外部キー）
        diff_id (ForeignKey): 難易度設定（m_diffモデルへの外部キー）
        created_at (DateTimeField): 作成日時
        updated_at (DateTimeField): 更新日時
    
    :return: スコア
    :rtype: str
    """
    score_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey('CustomUser',on_delete=models.SET_NULL,null=True,blank=True)
    score = models.IntegerField(default=0)
    lang_id=models.ForeignKey('m_lang', on_delete=models.SET_NULL, null=True, blank=True)
    diff_id=models.ForeignKey('m_diff',on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.score
    
class Rank(models.Model):
    """
    ランクマスタテーブル定義

    Attributes:
        rank_id (ForeignKey): ランクID
        rank (CharField): ランク名（appsの方でランクの初期値をメンバーに設定）
        created_at (DateTimeField): 作成日時
        updated_at (DateTimeField): 更新日時

    :return: ランクID、ランク名
    :rtype: str
    """
    rank_id = models.AutoField(primary_key=True)
    rank = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.rank_id} {self.rank}"