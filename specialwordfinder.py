from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """
        >>> special = SpecialWordFinder('words.txt')
        235890 words read

        >>> print("#" in special.words)
        False

        >>> isinstance(special.random(), str)
        True
    
    """

    def parse(self):
        w = super().parse()

        return [word for word in w if "#" not in word and word != '']


