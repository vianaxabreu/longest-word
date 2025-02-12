# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import string
import random
#challenge 3
import requests


class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()  # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        # challenge 3
        is_english = self.__check_dictionary(word)
        return is_english

    #challenge 3
    def __check_dictionary(self, word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response["found"]
