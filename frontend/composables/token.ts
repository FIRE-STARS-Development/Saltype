// トークンを保存する
export function saveToken(token: string) {
    localStorage.setItem('accessToken', token);
}

// トークンを取得する
export function getToken(): string | null {
    return localStorage.getItem('accessToken');
}

// トークンを削除する
export function removeToken() {
    localStorage.removeItem('accessToken');
}

// トークンの存在を確認する
export function isTokenAvailable(): boolean {
    return getToken() !== null;
}