from enum import Enum


class AnsiFormatting(int, Enum):
	NORMAL = 0
	BOLD = 1
	UNDERLINE = 4
	BLINKING = 5
