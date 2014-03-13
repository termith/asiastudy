class Text:
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
        return "Text({0})".format(self.value)

    def __len__(self):
        return len(self.value)

    def remove_spaces_from_text(self):
        self.value = self.value.replace("　", "").replace(" ", "")

    def remove_kana_symbols(self):
        with open('katakana', 'r', encoding='utf-8') as fd:
            katakana_list = fd.read().splitlines()
        with open('hiragana', 'r', encoding='utf-8') as fd:
            hiragana_list = fd.read().splitlines()
        with open('symbols', 'r', encoding='utf-8') as fd:
            symbols_list = fd.read().splitlines()
        for items in katakana_list:
            self.value = self.value.replace(items, "")
            for symb in hiragana_list:
                self.value = self.value.replace(symb, "")
                for symb in symbols_list:
                    self.value = self.value.replace(symb, "")

    def take_percent_count(self):
        total = len(self.value)
        N5 = self.each_level_kanji('kanji_n5')
        N4 = self.each_level_kanji('kanji_n4')
        N3 = self.each_level_kanji('kanji_n3')
        N2 = self.each_level_kanji('kanji_n2')
        N1 = self.each_level_kanji('kanji_n1')
        print("N1:", take_percent(total, N1))
        print("N2:", take_percent(total, N2))
        print("N3:", take_percent(total, N3))
        print("N4:", take_percent(total, N4))
        print("N5:", take_percent(total, N5))

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
    return  "{0}%".format(round((b/a)*100))


def take_string(file):
    with open(file, 'r', encoding='utf-8') as fd:
        return fd.read()


def main():
    input_text = Text(take_string('text_on_test'))
    input_text.remove_spaces_from_text()
    input_text.remove_kana_symbols()
    print(input_text)
    input_text.take_percent_count()