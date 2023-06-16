import sys

class Error:
    def __init__(self, text):
        self.text = text

    def print(self):
        return self.text