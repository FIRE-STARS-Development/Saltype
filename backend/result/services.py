from .models import Score

class ScoreService:
    def __init__(self, user_id, lang_id, diff_id, score):
        """
        初期化処理
        :param user_id: ユーザーID
        :param lang_id: 言語ID
        :param diff_id: 難易度ID
        :param score: 取得スコア
        """
        self.user_id = user_id
        self.lang_id = lang_id
        self.diff_id = diff_id
        self.score = score

    def is_new_high_score(self):
        """
        最高スコア判定処理
        
        :return: 
            is_high_score: 最高スコアかどうかのフラグ (bool)
            new_highest_score: 新しい最高スコア (int or None)
        """

        old_highest_score = Score.objects.filter(
            user_id=self.user_id,
            lang_id=self.lang_id,
            diff_id=self.diff_id
        ).order_by('-score', '-created_at').first()
        
        if old_highest_score is None: #過去スコアがない場合
            return True, self.score
        elif self.score > old_highest_score.score:#取得スコアが過去スコアより大きい場合
            return True, self.score
        else:#取得スコアの方が小さい場合
            return False, None

    def determine_rank(self):
        """
        スコアに基づいてランクIDを決定する
        
        :return: ランクID (int)
        """
        if self.score >= 1000:
            """7:社長"""
            return 7  
        elif self.score >= 900:
            """6:取締役"""
            return 6  
        elif self.score >= 700:
            """5:部長"""
            return 5  
        elif self.score >= 500:
            """4:課長"""
            return 4  
        elif self.score >= 300:
            """3:係長"""
            return 3  
        elif self.score >= 100:
            """2:主任"""
            return 2  
        else:
            """メンバー"""
            return 1  

    def get_ranking_position(self):
        """
        現在のユーザーのランキング順位を取得(タイ順位を採用)
        """
        
        """ ユーザーの最高スコアを取得 """
        user_score = Score.objects.filter(
            user_id=self.user_id,
            lang_id=self.lang_id,
            diff_id=self.diff_id
        ).order_by('-created_at').first()

        """ ユーザーのスコアより高いスコアを持つユーザーの数をカウント """
        higher_score_count = Score.objects.filter(
            lang_id=self.lang_id,
            diff_id=self.diff_id,
            score__gt=user_score.score
        ).count()

        """ 順位計算 """
        rank_position = higher_score_count + 1

        return rank_position