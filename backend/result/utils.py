from .models import Score
import logging
logger = logging.getLogger(__name__)

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

        logger.info(f"Checking new high score for user_id: {self.user_id}, lang_id: {self.lang_id}, diff_id: {self.diff_id}, score: {self.score}")
        """ 過去の最高スコアを取得 """
        old_highest_score = Score.objects.filter(
            user_id=self.user_id,
            lang_id=self.lang_id,
            diff_id=self.diff_id
        ).order_by('-score').first()


        """ 取得スコアが最高スコアかどうか判定 """
        if old_highest_score is None or self.score > old_highest_score.score:
            return True, self.score
        else:
            return False, None


    def determine_rank(self):
        """
        スコアに基づいてランクIDを決定する
        :return: ランクID (int)
        """
        if self.score >= 1000:
            return 7  # 社長 
        elif self.score >= 900:
            return 6  # 取締役
        elif self.score >= 700:
            return 5  # 部長
        elif self.score >= 500:
            return 4  # 課長
        elif self.score >= 300:
            return 3  # 係長
        elif self.score >= 100:
            return 2  # 主任
        else:
            return 1  # メンバー
