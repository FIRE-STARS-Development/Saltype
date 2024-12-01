/**
 * 受け渡した文字の変換(英語)
 * 1 → japanese, 2 → english
 * 数字 → 文字
 * @param language
 * @returns languageMap[language.toLowerCase()] || language
 */
export function convertNumberToEnglishLanguageName(
  languageCode: string
): string {
  const languageMap: { [key: string]: string } = {
    "1": "japanese",
    "2": "english",
  };
  return languageMap[languageCode.toLowerCase()] || languageCode;
}

/**
 * 受け渡した文字の変換(英語)
 * 1 → easy, 2 → normal, 3 → hard
 * 数字 → 文字
 * @param difficultyLevel
 * @returns difficultyMap[difficultyLevel.toLowerCase()] || difficultyLevel
 */
export function convertNumberToEnglishDifficultyLevelName(
  difficultyLevelCode: string
): string {
  const difficultyMap: { [key: string]: string } = {
    "1": "easy",
    "2": "normal",
    "3": "hard",
  };
  return (
    difficultyMap[difficultyLevelCode.toLowerCase()] || difficultyLevelCode
  );
}

/**
 * 受け渡した文字の変換(日本語)
 * 1 → 日本語, 2 → 英語
 * 数字 → 文字
 * @param language
 * @returns languageMap[language.toLowerCase()] || language
 */
export function convertNumberToJapaneseLanguageName(
  languageCode: string
): string {
  const languageMap: { [key: string]: string } = {
    "1": "日本語",
    "2": "英語",
  };
  return languageMap[languageCode.toLowerCase()] || languageCode;
}

/**
 * 受け渡した文字の変換(日本語)
 * 1 → イージー, 2 → ノーマル, 3 → ハード
 * 数字 → 文字
 * @param difficultyLevel
 * @returns difficultyMap[difficultyLevel.toLowerCase()] || difficultyLevel
 */
export function convertNumberToJapaneseDifficultyLevelName(
  difficultyLevelCode: string
): string {
  const difficultyMap: { [key: string]: string } = {
    "1": "イージー",
    "2": "ノーマル",
    "3": "ハード",
  };
  return (
    difficultyMap[difficultyLevelCode.toLowerCase()] || difficultyLevelCode
  );
}