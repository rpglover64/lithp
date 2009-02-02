import string
import re

from atom import Symbol
from atom import String
from number import Number, Integral, LongInt, Float

class Scanner:
    def __init__(self, str=None):
       print("Initializing the scanner...")
       self.raw_source = str
       self.index = 0
       self.length = 0
       self.sexpr = []

       if str:
           self.sexpr = self.get_sexpr()

    def get_sexpr(self, source=None):
        if source:
            self.raw_source = source
            self.length = len(self.raw_source)
            self.index = 0

        return self.get_token()

    def get_token(self):
        if self.index >= self.length:
            return None

        # Kill whitespace
        while self.index < self.length and self.raw_source[self.index] in string.whitespace:
            self.index = self.index + 1

        # Check if we had a string of whitespace
        if self.index == self.length:
            return None       

        token_str = ""
        
        # Build the token string
        while self.index < self.length:
            token_str = token_str + self.raw_source[self.index]
            self.index = self.index + 1

        if Integral.REGEX.match(token_str):
            return Integral(int(token_str))
        elif Float.REGEX.match(token_str):
            return Float(float(token_str))
        elif LongInt.REGEX.match(token_str):
            return LongInt(int(token_str))
        else:
            return Symbol(token_str)

        return None
