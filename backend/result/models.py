from django.db import models

class Lang(models.Model):
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
    lang_id = models.AutoField(primary_key=True)
    lang = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    class Meta:
        db_table = "m_lang"

class Diff(models.Model):
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
    diff_id = models.AutoField(primary_key=True)
    diff = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    class Meta:
        db_table = "m_diff"

class Rank(models.Model):
    """
    ランクマスタテーブル定義

    Attributes:
        rank_id (AutoField): ランクID
        rank (CharField): ランク名（初期パラーメータ所持-app.py参照）
        created_at (DateTimeField): 作成日時
        updated_at (DateTimeField): 更新日時
        del_flg (BooleanField): 削除フラグ
    
    Meta:
        db_table (str): データベーステーブル名
    """
    rank_id = models.AutoField(primary_key=True)
    rank = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    del_flg = models.BooleanField(default=False)

    class Meta:
        db_table = "m_rank"

class Score(models.Model):
    """
    スコアテーブル定義

    Attributes:
        score_id (AutoField): スコアID
        user (ForeignKey): スコアを記録したユーザーID（Userモデルへの外部キー）
        score (IntegerField): ゲームのスコア（デフォルトで0）
        lang (ForeignKey): 言語設定（Langモデルへの外部キー）
        diff (ForeignKey): 難易度設定（Diffモデルへの外部キー）
        created_at (DateTimeField): 作成日時
        updated_at (DateTimeField): 更新日時
    
    Meta:
        db_table (str): データベーステーブル名
    """
    score_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    score = models.IntegerField(default=0)
    lang = models.ForeignKey('Lang', on_delete=models.SET_NULL, null=True, blank=True)
    diff = models.ForeignKey('Diff', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "t_score"

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    rank = models.ForeignKey('Rank', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "m_user"
