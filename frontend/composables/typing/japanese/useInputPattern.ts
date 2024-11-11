/**
 * 単一文字入力パターン
 * @returns getPatternArray
 */
export function useInputPattern() {
  const japaneseInputPattern: [string, string[]][] = [
    ["あ", ["a"]],
    ["い", ["i"]],
    ["う", ["u"]],
    ["え", ["e"]],
    ["お", ["o"]],
    ["か", ["ka", "ca"]],
    ["き", ["ki"]],
    ["く", ["ku", "cu"]],
    ["け", ["ke"]],
    ["こ", ["ko", "co"]],
    ["さ", ["sa"]],
    ["し", ["shi", "si", "ci"]],
    ["す", ["su"]],
    ["せ", ["se"]],
    ["そ", ["so"]],
    ["た", ["ta"]],
    ["ち", ["chi", "ti"]],
    ["つ", ["tsu", "tu"]],
    ["て", ["te"]],
    ["と", ["to"]],
    ["な", ["na"]],
    ["に", ["ni"]],
    ["ぬ", ["nu"]],
    ["ね", ["ne"]],
    ["の", ["no"]],
    ["は", ["ha"]],
    ["ひ", ["hi"]],
    ["ふ", ["fu", "hu"]],
    ["へ", ["he"]],
    ["ほ", ["ho"]],
    ["ま", ["ma"]],
    ["み", ["mi"]],
    ["む", ["mu"]],
    ["め", ["me"]],
    ["も", ["mo"]],
    ["や", ["ya"]],
    ["ゆ", ["yu"]],
    ["よ", ["yo"]],
    ["ら", ["ra"]],
    ["り", ["ri"]],
    ["る", ["ru"]],
    ["れ", ["re"]],
    ["ろ", ["ro"]],
    ["わ", ["wa"]],
    ["を", ["wo"]],
    ["ん", ["nn", "n"]],
    ["が", ["ga"]],
    ["ぎ", ["gi"]],
    ["ぐ", ["gu"]],
    ["げ", ["ge"]],
    ["ご", ["go"]],
    ["ざ", ["za"]],
    ["じ", ["ji", "zi", "jyi"]],
    ["ず", ["zu"]],
    ["ぜ", ["ze"]],
    ["ぞ", ["zo"]],
    ["だ", ["da"]],
    ["ぢ", ["di", "dyi"]],
    ["づ", ["du", "dzu"]],
    ["で", ["de"]],
    ["ど", ["do"]],
    ["ば", ["ba"]],
    ["び", ["bi"]],
    ["ぶ", ["bu"]],
    ["べ", ["be"]],
    ["ぼ", ["bo"]],
    ["ぱ", ["pa"]],
    ["ぴ", ["pi"]],
    ["ぷ", ["pu"]],
    ["ぺ", ["pe"]],
    ["ぽ", ["po"]],
    ["きゃ", ["kya"]],
    ["きゅ", ["kyu"]],
    ["きょ", ["kyo"]],
    ["しゃ", ["sha", "sya"]],
    ["しゅ", ["shu", "syu"]],
    ["しょ", ["sho", "syo"]],
    ["ちゃ", ["cha", "tya"]],
    ["ちゅ", ["chu", "tyu"]],
    ["ちょ", ["cho", "tyo"]],
    ["にゃ", ["nya"]],
    ["にゅ", ["nyu"]],
    ["にょ", ["nyo"]],
    ["ひゃ", ["hya"]],
    ["ひゅ", ["hyu"]],
    ["ひょ", ["hyo"]],
    ["みゃ", ["mya"]],
    ["みゅ", ["myu"]],
    ["みょ", ["myo"]],
    ["りゃ", ["rya"]],
    ["りゅ", ["ryu"]],
    ["りょ", ["ryo"]],
    ["ぎゃ", ["gya"]],
    ["ぎゅ", ["gyu"]],
    ["ぎょ", ["gyo"]],
    ["じゃ", ["ja", "jya"]],
    ["じゅ", ["ju", "jyu"]],
    ["じょ", ["jo", "jyo"]],
    ["びゃ", ["bya"]],
    ["びゅ", ["byu"]],
    ["びょ", ["byo"]],
    ["ぴゃ", ["pya"]],
    ["ぴゅ", ["pyu"]],
    ["ぴょ", ["pyo"]],
    ["ぁ", ["xa", "la"]],
    ["ぃ", ["xi", "li"]],
    ["ぅ", ["xu", "lu"]],
    ["ぇ", ["xe", "le"]],
    ["ぉ", ["xo", "lo"]],
    ["っ", ["xtu", "xtsu", "ltu", "ltsu"]],
    ["ゃ", ["xya", "lya"]],
    ["ゅ", ["xyu", "lyu"]],
    ["ょ", ["xyo", "lyo"]],
    ["ゎ", ["xwa", "lwa"]],
    ["ゐ", ["wi"]],
    ["ゑ", ["we"]],
    ["ヴぁ", ["va"]],
    ["ヴぃ", ["vi"]],
    ["ヴ", ["vu"]],
    ["ヴぇ", ["ve"]],
    ["ヴぉ", ["vo"]],
    ["てぃ", ["thi"]],
    ["でぃ", ["dhi"]],
    ["でゅ", ["dhu"]],
    ["ふぁ", ["fa"]],
    ["ふぃ", ["fi"]],
    ["ふぇ", ["fe"]],
    ["ふぉ", ["fo"]],
    ["っか", ["kka", "cca"]],
    ["っき", ["kki"]],
    ["っく", ["kku", "ccu"]],
    ["っけ", ["kke"]],
    ["っこ", ["kko", "cco"]],
    ["っさ", ["ssa"]],
    ["っし", ["sshi", "ssi"]],
    ["っす", ["ssu"]],
    ["っせ", ["sse"]],
    ["っそ", ["sso"]],
    ["った", ["tta"]],
    ["っち", ["cchi", "tti"]],
    ["っつ", ["ttsu", "ttu"]],
    ["って", ["tte"]],
    ["っと", ["tto"]],
    ["っは", ["hha"]],
    ["っひ", ["hhi"]],
    ["っふ", ["ffu", "hhu"]],
    ["っへ", ["hhe"]],
    ["っほ", ["hho"]],
    ["っぱ", ["ppa"]],
    ["っぴ", ["ppi"]],
    ["っぷ", ["ppu"]],
    ["っぺ", ["ppe"]],
    ["っぽ", ["ppo"]],
    ["っば", ["bba"]],
    ["っび", ["bbi"]],
    ["っぶ", ["bbu"]],
    ["っべ", ["bbe"]],
    ["っぼ", ["bbo"]],
    ["っま", ["mma"]],
    ["っみ", ["mmi"]],
    ["っむ", ["mmu"]],
    ["っめ", ["mme"]],
    ["っも", ["mmo"]],
    ["っや", ["yya"]],
    ["っゆ", ["yyu"]],
    ["っよ", ["yyo"]],
    ["っら", ["rra"]],
    ["っり", ["rri"]],
    ["っる", ["rru"]],
    ["っれ", ["rre"]],
    ["っろ", ["rro"]],
    ["っわ", ["wwa"]],
    ["っが", ["gga"]],
    ["っぎ", ["ggi"]],
    ["っぐ", ["ggu"]],
    ["っげ", ["gge"]],
    ["っご", ["ggo"]],
    ["っざ", ["zza"]],
    ["っじ", ["jji", "zzi"]],
    ["っず", ["zzu"]],
    ["っぜ", ["zze"]],
    ["っぞ", ["zzo"]],
    ["っだ", ["dda"]],
    ["っぢ", ["ddi"]],
    ["っづ", ["ddu"]],
    ["っで", ["dde"]],
    ["っど", ["ddo"]],
    ["っしょ", ["ssyo", "sshyo"]],
    ["？", ["?"]],
    ["、", [","]],
    ["。", ["."]],
    ["ー", ["-"]],
  ];

  const vowelInputPattern: string[] = ["a", "i", "u", "e", "o"];

  function getPatternArray() {
    return japaneseInputPattern;
  }

  function getVowelPatternArray() {
    return vowelInputPattern;
  }

  return {
    getPatternArray,
    getVowelPatternArray,
  };
}
