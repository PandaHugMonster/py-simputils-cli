from collections.abc import Callable
from typing import AnyStr

from typing_extensions import Any

from simputils.cli.components.CliTextBlock import CliTextBlock
from simputils.cli.components.CliTextConfig import CliTextConfig
from simputils.cli.utils.cli import regex_match_cli_special_chars


class SimpleCliTableRow:
	cells: list[str]
	data: dict | None
	_cols_formatting: dict[int, CliTextConfig | Callable] | CliTextConfig | Callable = None
	_col_pad_counts: dict[int, int] = None
	content_pad_char: str = " "

	padding_right_char: str = " "
	padding_right_count: int = 3

	padding_left_char: str = " "
	padding_left_count: int = 0

	border_vertical_char: str = None

	def __init__(
		self,
		*text: AnyStr | Any | CliTextBlock,

		col_pad_counts: dict[int, int] = None,
		data: dict = None,
		content_pad_char: str = " ",

		padding_right_char: str = " ",
		padding_right_count: int = 2,

		padding_left_char: str = " ",
		padding_left_count: int = 2,

		border_vertical_char: str = None,
		cols_formatting: dict[int, CliTextConfig | Callable] | CliTextConfig | Callable = None,

	):
		self.cells = list(text)
		self.data = data
		self._cols_formatting = cols_formatting or {}
		self._col_pad_counts = col_pad_counts if col_pad_counts is not None else {}

		self.content_pad_char = content_pad_char
		self.padding_right_char = padding_right_char
		self.padding_right_count = padding_right_count
		self.padding_left_char = padding_left_char
		self.padding_left_count = padding_left_count
		self.border_vertical_char = border_vertical_char

	def render(self):
		res = ""
		data = self.data if self.data is not None else {}

		for i, text in enumerate(self.cells):
			if isinstance(text, str):
				text = f"{text}".format(**data)

			formatter = None
			if isinstance(self._cols_formatting, dict) and i in self._cols_formatting and self._cols_formatting[i]:
				formatter = self._cols_formatting[i]
			elif callable(self._cols_formatting):
				formatter = self._cols_formatting

			if formatter and (not isinstance(text, str) or not regex_match_cli_special_chars.match(text)):
				text = formatter(text, i)

			text = f"{text}"

			if self._col_pad_counts and i < len(self._col_pad_counts):
				clear_length = len(regex_match_cli_special_chars.sub('', text))
				max_length = self._col_pad_counts[i] if self._col_pad_counts[i] is not None else 0
				extension = max_length - clear_length
				if extension != 0:
					text = f"{text}{extension * self.content_pad_char}"

			if res and self.border_vertical_char:
				res += self.border_vertical_char

			res += (f"{self.padding_left_char * self.padding_left_count}"
			        f"{text}"
			        f"{self.padding_right_char * self.padding_right_count}")

		return res
