#!/usr/bin/python
# coding=utf-8

class Kanjies_text:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return "Kanjies_text({0})".format(self.value)

    def __len__(self):
        return len(self.value)

    def remove_spaces_from_text(self):
        self.value = self.value.replace("　", "").replace(" ", "")

    def remove_kana_symbols(self):
        hira = [u'が', u'ぎ', u'ぐ', u'げ', u'ご', u'ざ', u'じ', u'ず', u'ぜ', u'ぞ', u'だ', u'ぢ', u'づ', u'で', u'ど',
                u'ば', u'び', u'ぶ', u'べ', u'ぼ', u'ぱ', u'ぴ', u'ぷ', u'ぺ', u'ぽ', u'あ', u'い', u'う', u'え', u'お',
                u'か', u'き', u'く', u'け', u'こ', u'さ', u'し', u'す', u'せ', u'そ', u'た', u'ち', u'つ', u'て', u'と',
                u'な', u'に', u'ぬ', u'ね', u'の', u'は', u'ひ', u'ふ', u'へ', u'ほ', u'ま', u'み', u'む', u'め', u'も',
                u'や', u'ゆ', u'よ', u'ら', u'り', u'る', u'れ', u'ろ', u'わ', u'を', u'ん', u'ぁ', u'ぃ', u'ぅ', u'ぇ',
                u'ぉ', u'ゃ', u'ゅ', u'ょ', u'っ']
        kata = [u'ガ', u'ギ', u'グ', u'ゲ', u'ゴ', u'ザ', u'ジ', u'ズ', u'ゼ', u'ゾ', u'ダ', u'ヂ', u'ヅ', u'デ', u'ド',
                u'バ', u'ビ', u'ブ', u'ベ', u'ボ', u'パ', u'ピ', u'プ', u'ペ', u'ポ', u'ア', u'イ', u'ウ', u'エ', u'オ',
                u'カ', u'キ', u'ク', u'ケ', u'コ', u'サ', u'シ', u'ス', u'セ', u'ソ', u'タ', u'チ', u'ツ', u'テ', u'ト',
                u'ナ', u'ニ', u'ヌ', u'ネ', u'ノ', u'ハ', u'ヒ', u'フ', u'ヘ', u'ホ', u'マ', u'ミ', u'ム', u'メ', u'モ',
                u'ヤ', u'ユ', u'ヨ', u'ラ', u'リ', u'ル', u'レ', u'ロ', u'ワ', u'ヲ', u'ン', u'ァ', u'ィ', u'ゥ', u'ェ',
                u'ォ', u'ャ', u'ュ', u'ョ', u'ッ']
        half = [u'ｶﾞ', u'ｷﾞ', u'ｸﾞ', u'ｹﾞ', u'ｺﾞ', u'ｻﾞ', u'ｼﾞ', u'ｽﾞ', u'ｾﾞ', u'ｿﾞ', u'ﾀﾞ', u'ﾁﾞ', u'ﾂﾞ', u'ﾃﾞ', u'ﾄﾞ',
                u'ﾊﾞ', u'ﾋﾞ', u'ﾌﾞ', u'ﾍﾞ', u'ﾎﾞ', u'ﾊﾟ', u'ﾋﾟ', u'ﾌﾟ', u'ﾍﾟ', u'ﾎﾟ', u'ｱ', u'ｲ', u'ｳ', u'ｴ', u'ｵ', u'ｶ',
                u'ｷ', u'ｸ', u'ｹ', u'ｺ', u'ｻ', u'ｼ', u'ｽ', u'ｾ', u'ｿ', u'ﾀ', u'ﾁ', u'ﾂ', u'ﾃ', u'ﾄ', u'ﾅ', u'ﾆ', u'ﾇ',
                u'ﾈ', u'ﾉ', u'ﾊ', u'ﾋ', u'ﾌ', u'ﾍ', u'ﾎ', u'ﾏ', u'ﾐ', u'ﾑ', u'ﾒ', u'ﾓ', u'ﾔ', u'ﾕ', u'ﾖ', u'ﾗ', u'ﾘ',
                u'ﾙ', u'ﾚ', u'ﾛ', u'ﾜ', u'ｦ', u'ﾝ', u'ｧ', u'ｨ', u'ｩ', u'ｪ', u'ｫ', u'ｬ', u'ｭ', u'ｮ', u'ｯ']
        kana = hira + kata + half

        wnum = [u'０', u'１', u'２', u'３', u'４', u'５', u'６', u'７', u'８', u'９']
        hnum = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9']
        walp = [u'ａ', u'ｂ', u'ｃ', u'ｄ', u'ｅ', u'ｆ', u'ｇ', u'ｈ', u'ｉ', u'ｊ', u'ｋ', u'ｌ', u'ｍ', u'ｎ', u'ｏ',
                u'ｐ', u'ｑ', u'ｒ', u'ｓ', u'ｔ', u'ｕ', u'ｖ', u'ｗ', u'ｘ', u'ｙ', u'ｚ', u'Ａ', u'Ｂ', u'Ｃ', u'Ｄ',
                u'Ｅ', u'Ｆ', u'Ｇ', u'Ｈ', u'Ｉ', u'Ｊ', u'Ｋ', u'Ｌ', u'Ｍ', u'Ｎ', u'Ｏ', u'Ｐ', u'Ｑ', u'Ｒ', u'Ｓ',
                u'Ｔ', u'Ｕ', u'Ｖ', u'Ｗ', u'Ｘ', u'Ｙ', u'Ｚ']
        halp = [u'a', u'b', u'c', u'd', u'e', u'f', u'g', u'h', u'i', u'j', u'k', u'l', u'm', u'n', u'o', u'p', u'q',
                u'r', u's', u't', u'u', u'v', u'w', u'x', u'y', u'z', u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H',
                u'I', u'J', u'K', u'L', u'M', u'N', u'O', u'P', u'Q', u'R', u'S', u'T', u'U', u'V', u'W', u'X', u'Y',
                u'Z']
        wsym = [u'！', u'”', u'＃', u'＄', u'％', u'＆', u'’', u'（', u'）', u'＊', u'＋', u'、', u'−', u'．', u'／',
                u'：', u'；', u'＜', u'＝', u'＞', u'？', u'＠', u'「', u'＼', u'」', u'＾', u'＿', u'｀', u'『', u'｜',
                u'』', u'〜', u'、', u'。']
        hsym = [u'!', u'\"', u'#', u'$', u'%', u'&', u'\'', u'(', u')', u'*', u'+', u',', u'-', u'.', u'/', u':', u';',
                u'<', u'=', u'>', u'?', u'@', u'[', u'\\', u']', u'^', u'_', u'`', u'{', u'|', u'}', u'~']
        symbols = wnum + hnum + walp + halp + wsym + hsym

        for items in kana:
            self.value = self.value.replace(items, "")
            for symb in symbols:
                self.value = self.value.replace(symb, "")

    def take_percent_count(self):
        total = len(self.value)
        N5 = self.each_level_kanji('core/kanji_n5')
        N4 = self.each_level_kanji('core/kanji_n4')
        N3 = self.each_level_kanji('core/kanji_n3')
        N2 = self.each_level_kanji('core/kanji_n2')
        N1 = self.each_level_kanji('core/kanji_n1')
        return [take_percent(total, N1), take_percent(total, N2), take_percent(total, N3), take_percent(total, N4),
                take_percent(total, N5)]

    def each_level_kanji(self, kanji_level_list):
        kanjis_this_level=0
        with open(kanji_level_list, 'r', encoding='utf-8') as fd:
            kanji_text = fd.read().splitlines()
        for items in kanji_text:
            counter = 0
            for i in range(len(self)):
                if items == self.value[i]:
                    counter = counter + 1
            if counter != 0:
                kanjis_this_level = counter + kanjis_this_level
        return kanjis_this_level


def take_percent(a, b):
    return "{0}%".format(round((b/a)*100))


def take_string(file):
    with open(file, 'r', encoding='utf-8') as fd:
        return fd.read()