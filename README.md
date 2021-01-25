# Introduction
**tty-color** is a Python package for manage a console colors

# Install
## Python pip
`pip install tty-color`

## Python direct install
* Download archive & extract
* `python setup.py install`

# Usage
## Import
`from ttycolor import Color`

Create an instance of **Color** class.
In examples, _color_ is instance of **Color**

## Standard ANSI colors
### print(text, code)
Print text with the ANSI code. Automatically add RESET ANSI code after text.

`color.print('Your text', CODE)`

**CODE** is a constant of Color class.

### color(text, code)
Return text with the ANSI code. Not automatically add RESET ANSI code.

`print(color.color('Your text', CODE)`

**CODE** is a constant of Color class.

## Extended ANSI colors
### printrgb(text, r, g, b, type)
Print text with the RGB color. Automatically add RESET ANSI code after text.

`color.printrgb('Your text', 255, 0, 0)`

In example, display a red text. If type not established, the FG (foreground) constant used.

Type is FG or BG constant. If used other value, the Foreground (FG constant) used.

### colorrgb(text, r, g, b, type)
Return text with the RGB color. Not automatically add RESET ANSI code.

`color.colorrgb('Your text', 0x0C, 0x0C, 0x0C, color.BG)`

In example, display a text with the grey background.
If type not established, the FG (foreground) constant used.

Type is FG or BG constant. If used other value, the Foreground (FG constant) used.

## List of standard ANSI code
* **RESET** : reset to the default color
* **BOLD** : bold text
* **FAINT**
* **ITALIC** : italic text
* **UNDERLINE** : underline text
* **SLOW_BLINK** : blink slowly (if console accept blink)
* **BLINK** : blink (if console accept blink)
* **BLACK** : black foreground color
* **RED** : red foreground color
* **GREEN** : green foreground color
* **YELLOW** : yellow foreground color
* **BLUE** : blue foreground color
* **MAGENTA** : magenta foreground color
* **CYAN** : cyan foreground color
* **WHITE** : white foreground color
* **GREY** : grey foreground color
* **LIGHT_RED** : light red foreground color
* **LIGHT_GREEN** : light green foreground color
* **LIGHT_YELLOW** : light yellow foreground color
* **LIGHT_BLUE** : light blue foreground color
* **LIGHT_MAGENTA** : light magenta foreground color
* **LIGHT_CYAN** : light cyan foreground color
* **LIGHT_WHITE** : light white foreground color
* All colors prefixed by : **BG_** is for background color

# Credits
Package developed by Christophe Daloz - De Los Rios <christophedlr@gmail.com>
