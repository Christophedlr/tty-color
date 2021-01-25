import platform
from multimethod import overload

if platform.system() == 'Windows':
    import os
    os.system('')


class Color:
    RESET: str = '0'
    BOLD: str = '1'
    FAINT: str = '2'
    ITALIC: str = '3'
    UNDERLINE: str = '4'
    SLOW_BLINK: str = '5'
    BLINK: str = '6'
    BLACK: str = '30'
    RED: str = '31'
    GREEN: str = '32'
    YELLOW: str = '33'
    BLUE: str = '34'
    MAGENTA: str = '35'
    CYAN: str = '36'
    WHITE: str = '37'
    BG_BLACK: str = '40'
    BG_RED: str = '41'
    BG_GREEN: str = '42'
    BG_YELLOW: str = '43'
    BG_BLUE: str = '44'
    BG_MAGENTA: str = '45'
    BG_CYAN: str = '46'
    BG_WHITE: str = '47'
    GREY: str = '90'
    LIGHT_RED: str = '91'
    LIGHT_GREEN: str = '92'
    LIGHT_YELLOW: str = '93'
    LIGHT_BLUE: str = '94'
    LIGHT_MAGENTA: str = '95'
    LIGHT_CYAN: str = '96'
    LIGHT_WHITE: str = '97'
    BG_GREY: str = '100'
    BG_LIGHT_RED: str = '101'
    BG_LIGHT_GREEN: str = '102'
    BG_LIGHT_YELLOW: str = '103'
    BG_LIGHT_BLUE: str = '104'
    BG_LIGHT_MAGENTA: str = '105'
    BG_LIGHT_CYAN: str = '106'
    BG_LIGHT_WHITE: str = '107'

    # Define the ANSI code
    def ansi(self, code: str) -> str:
        return '\033['+code+'m'

    # print text with ANSI code
    @overload
    def print(self, text: str, code: str):
        print(self.ansi(code)+text+self.ansi(self.RESET))
