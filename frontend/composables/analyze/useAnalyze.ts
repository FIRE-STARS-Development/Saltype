import { useUser } from "../conf/useUser";
import { useUserInfo } from "../server/useUserInfo";

export function useAnalyze() {
  const config = useRuntimeConfig();
  const { user } = useUser();
  const { waitForUser } = useUserInfo();
  const typoFrequency = ref<TypoFrequency[]>([]);

  interface TypoFrequency {
    miss_char: string;
    miss_count: number;
  }

  const getTypoFrequencyByLimitParam = async (limit: Number) => {
    try {
      await waitForUser();

      if (!user.value) {
        console.error("ユーザ情報が存在しません");
        return;
      }

      const response = await fetch(
        `${config.public.baseURL}/api/django/mistype/top/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            user_id: user.value.user_id,
            limit: limit,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("ミスタイプ頻度の取得に失敗しました");
      }

      const data = await response.json();

      typoFrequency.value = data.top_mistypes;
    } catch (e) {
      console.error(e);
    }
  };

  const getPastScores = async (
    selectedLanguage: Number,
    selectedDifficulty: Number
  ) => {
    try {
      await waitForUser();

      if (!user.value) {
        console.error("ユーザ情報が存在しません");
        return;
      }

      const response = await fetch(
        `${config.public.baseURL}/api/django/score/past-scores/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            user_id: user.value.user_id,
            lang_id: selectedLanguage,
            diff_id: selectedDifficulty,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("過去のスコア取得に失敗しました");
      }

      const data = await response.json();

      return data.scores;
    } catch (e) {
      console.error(e);
    }
  };

  return {
    typoFrequency,
    getTypoFrequencyByLimitParam,
    getPastScores,
  };
}
