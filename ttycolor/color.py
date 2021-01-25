import platform

if platform.system() == 'Windows':
    import os

    os.system('')


# Color manager
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
    FG: str = '38'
    BG_BLACK: str = '40'
    BG_RED: str = '41'
    BG_GREEN: str = '42'
    BG_YELLOW: str = '43'
    BG_BLUE: str = '44'
    BG_MAGENTA: str = '45'
    BG_CYAN: str = '46'
    BG_WHITE: str = '47'
    BG: str = '48'
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
        return '\033[' + code + 'm'

    # Return color text with ANSI standard code
    def color(self, text: str, code: str) -> str:
        return self.ansi(code) + text

    # Return color text with ANSI extended code
    def colorrgb(self, text: str, r: int, g: int, b: int, type: str = FG) -> str:
        if r > 255 or r < 0:
            r = 0

        if g > 255 or g < 0:
            g = 0

        if b > 255 or b < 0:
            b = 0

        if type == self.FG or type == self.BG:
            code = type + ';2;' + str(r) + ';' + str(g) + ';' + str(b)
        else:
            code = '38;2;' + str(r) + ';' + str(g) + ';' + str(b)

        return self.ansi(code) + text

    # print text with ANSI code
    def print(self, text: str, code: str):
        print(self.ansi(code) + text + self.ansi(self.RESET))

    # Print text with extended colors in RGB
    def printrgb(self, text: str, r: int, g: int, b: int, type: str = FG):
        print(self.colorrgb(text, r, g, b, type) + self.ansi(self.RESET))
