import {
    getAuth,
    GoogleAuthProvider,
    signInWithRedirect,
    getRedirectResult,
    signOut as firebaseSignOut,
    type UserCredential
} from 'firebase/auth'
import app from "../firebase";
import { useUser } from '../composables/user'

type Auth = {
    signIn: () => Promise<void>
    signOut: () => Promise<void>
}

export const useAuth = (): Auth => {
    const { setUser } = useUser()

    const signIn = async (): Promise<void> => {
        const auth = getAuth(app);
        const provider = new GoogleAuthProvider();
        try {
            await signInWithRedirect(auth, provider)
                .then((result: UserCredential) => {
                    setUser(result.user);
                })
        } catch (error) {
            if (error instanceof Error && error.message.includes('auth/popup-closed-by-user')) {
                console.log('Google認証のポップアップを閉じました');
                //認証を中断したことをCompositionAPIで表示
            } else {
                console.error('Error during sign-in:', error); //dev only
                alert('エラーが発生しました。もう一度お試しください。');
            }
        }
    };

    // リダイレクト後に結果を取得
    const handleRedirectResult = async (): Promise<void> => {
        const auth = getAuth(app);
        try {
            const result = await getRedirectResult(auth);
            if (result) {
                const user = result.user;
                setUser(user);
                console.log('User signed in:', user); //dev only
            }
        } catch (error) {
            console.error('Error during handling redirect result:', error); //dev only
        }
    };

    const signOut = async (): Promise<void> => {
        const auth = getAuth();
        await firebaseSignOut(auth)
            .then(() => {
                setUser(null);
            })
            .catch((error) => {
                console.log(error); //dev only
                alert(error.message); //dev only
            });
    };

    window.onload = handleRedirectResult;

    return {
        signIn,
        signOut
    }
}