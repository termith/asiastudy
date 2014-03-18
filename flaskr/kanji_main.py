#!/usr/bin/python
# coding=utf-8

from static_data_for_application import AnalyzerData

class KanjiesText:
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
        return "KanjiesText({0})".format(self.value)

    def __len__(self):
        return len(self.value)

    def remove_spaces_from_text(self):
        self.value = self.value.replace("　", "").replace(" ", "")

    def remove_kana_symbols(self):
        for items in AnalyzerData.KANA:
            self.value = self.value.replace(items, "")
            for symb in AnalyzerData.SYMBOLS:
                self.value = self.value.replace(symb, "")

    def take_percent_count(self):
        total = len(self.value)
        N5 = self.each_level_kanji(AnalyzerData.KANJI_JLPT_5)
        N4 = self.each_level_kanji(AnalyzerData.KANJI_JLPT_4)
        N3 = self.each_level_kanji(AnalyzerData.KANJI_JLPT_3)
        N2 = self.each_level_kanji(AnalyzerData.KANJI_JLPT_2)
        N1 = self.each_level_kanji(AnalyzerData.KANJI_JLPT_1)
        return [take_percent(total, N1), take_percent(total, N2), take_percent(total, N3), take_percent(total, N4),
                take_percent(total, N5)]

    def each_level_kanji(self, kanji_level_list):
        kanjis_this_level=0
        for items in kanji_level_list:
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