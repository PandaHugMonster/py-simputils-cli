from enum import Enum


class AnsiBackgroundColor(int, Enum):
	RESET = 0
	BLACK = 40
	RED = 41
	GREEN = 42
	BROWN = 43
	BLUE = 44
	PURPLE = 45
	CYAN = 46
	GRAY = 47