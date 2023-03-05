"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """
        >>> words = WordFinder('words.txt')
        235893 words read

        >>> isinstance(words.random(), str)
        True


    """
    def __init__(self, path) -> None:
        """Takes in a path string to read and parse lines"""
        self.path = path
        self.file = open(path)
        self.words = self.parse()
        self.read_num()
    
    def parse(self):
        """Uses file object to read and splitlines on newline"""
        return self.file.read().splitlines()

    def read_num(self):
        """Prints out the number of words read from file"""
        print(f'{len(self.words)} words read')
    
    def random(self):
        """Selects a random word and returns it"""
        return choice(self.words)
