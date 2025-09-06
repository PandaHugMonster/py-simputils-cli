from collections.abc import Callable

from typing_extensions import Any

from simputils.cli.components.CliTextConfig import CliTextConfig
from simputils.cli.components.SimpleCliTableRow import SimpleCliTableRow
from simputils.cli.utils.cli import regex_match_cli_special_chars


class SimpleCliTable:
	_rows: list[SimpleCliTableRow] = None
	_cache: list[str] = None
	_col_pad_counts: dict[int, int] = None
	_cols_formatting: dict[int, CliTextConfig] = None
	debug_paddings: bool = False

	content_pad_char = "%"

	padding_left_char = "<"
	padding_left_count = 5

	padding_right_char = ">"
	padding_right_count = 5

	mutator: Callable = None

	# MARK  Plan:
	#       * Need cache with data ready to be used, so all the paddings are correct
	#       * Mutator must be applied beforehand, so all the updated max lengths are known

	def __init__(
		self,
		content_pad_char="%",

		padding_left_char="<",
		padding_left_count=5,

		padding_right_char=">",
		padding_right_count=5,
		mutator: Callable = None,
	):
		self._rows = []
		self._col_pad_counts = {}
		self._cols_formatting = {}
		self.mutator = mutator

		self.content_pad_char = content_pad_char
		self.padding_left_char = padding_left_char
		self.padding_left_count = padding_left_count
		self.padding_right_char = padding_right_char
		self.padding_right_count = padding_right_count

	def set_col_formatting(self, col: int, config: CliTextConfig | None):
		if col not in self._cols_formatting and config is None:
			return

		if col in self._cols_formatting and config is None:
			del self._cols_formatting[col]
			return

		self._cols_formatting[col] = config

	def add_row(self, *text: Any, data: dict = None):
		row = SimpleCliTableRow(
			*text,
			data=data,

			col_pad_counts=self._col_pad_counts,
			content_pad_char=self.content_pad_char,

			padding_left_char=self.padding_left_char,
			padding_left_count=self.padding_left_count,

			padding_right_char=self.padding_right_char,
			padding_right_count=self.padding_right_count,
		)

		self._rows.append(row)

		self._update_cache(row)

	def _update_cache(self, row: SimpleCliTableRow):
		max_lengths_length = len(self._col_pad_counts)
		orig_str = str(row)
		stripped_str = regex_match_cli_special_chars.sub("", orig_str)

		val_len = len(stripped_str)

		if val_len < 1:
			return

		if max_lengths_length > i:
			orig_value = self._cell_max_lengths[i]
			self._cell_max_lengths[i] = max(orig_value, val_len)
		else:
			self._cell_max_lengths.append(val_len)

	def __str__(self):
		res = ""

		for row in self._rows:
			# row_res = ""
			# data = row.data
			# if data is None:
			# 	data = {}
			# # if self._mutator:
			# # 	mutated_res = self._mutator
			# for i, text in enumerate(row.cells):
			# 	text = f"{text}".format(**data)
			#
			# 	if i in self._cols_formatting and self._cols_formatting[i]:
			# 		formatter = self._cols_formatting[i]
			# 		if not ansi_escape_8bit.match(text):
			# 			text = formatter(text)
			#
			# 	exp_length = self._cell_max_lengths[i]
			# 	extension = exp_length - len(ansi_escape_8bit.sub('', text))
			# 	if extension != 0:
			# 		symb1 = ' ' if not self.debug_paddings else '#'
			# 		text = f"{text}{extension * symb1}"
			#
			# 	symb2 = ' ' if not self.debug_paddings else '*'
			# 	row_res += f"{text}{self.padding_right * symb2}"

			res += f"{row_res}\n"

		return res
