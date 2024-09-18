import { ref } from "vue";
import { useRouter } from "vue-router";
import { useToken } from "./useToken";
import { useRuntimeConfig } from "nuxt/app";
import { useSession } from "../server/useSession";

/**
 * オリジナルフォームログイン処理
 * @returns login, isLoading, error
 */
export async function useLogin() {
  const config = useRuntimeConfig();
  const { saveToken } = useToken();
  const { saveSession } = useSession();
  const router = useRouter();
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  //オリジナルフォームログイン処理
  const login = async (email: string, password: string) => {
    isLoading.value = true;
    error.value = null;

    try {
      const response = await fetch(`${config.public.baseURL}/api/login/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: email,
          password: password,
        }),
        signal: AbortSignal.timeout(5000),
      });

      if (response.ok) {
        const data = await response.json();
        if (data.token) {
          saveToken(data.token);
          saveSession(data);
          router.push({ name: "home" });
        } else {
          error.value = "トークンが発行されませんでした";
        }
      } else {
        const errorData = await response.json();
        error.value = errorData.message || "ログインに失敗しました。";
      }
    } catch (err) {
      error.value =
        "ネットワークエラーが発生しました。接続を確認してください。";
    } finally {
      isLoading.value = false;
    }
  };

  return {
    login,
    isLoading,
    error,
  };
}