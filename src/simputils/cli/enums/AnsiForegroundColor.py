from enum import Enum


class AnsiForegroundColor(int, Enum):
	RESET = 0
	BLACK = 30
	RED = 31
	GREEN = 32
	BROWN = 33
	BLUE = 34
	PURPLE = 35
	CYAN = 36
	GRAY = 37