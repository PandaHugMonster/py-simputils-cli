from collections.abc import Callable

from typing_extensions import Any

from simputils.cli.components.SimpleCliTableRow import SimpleCliTableRow
from simputils.cli.utils.cli import regex_match_cli_special_chars


class SimpleCliTable:

	_rows_raw: list[tuple[Any, ...]] = None
	_cells_formatting: Callable = None
	# _cell_max_lengths: list[int] = None
	_cell_lengths: dict[int, int] = None

	def __init__(self, *, cells_formatting: Callable | None = None):
		self._rows_raw = []
		self._cells_formatting = cells_formatting
		self._cell_lengths = {}
		# self._cell_max_lengths = []

	def add_row(self, *cells):
		self._rows_raw.append(cells)
		self._update_cache(cells)

	def _update_cache(self, cells: tuple | list):
		for i, cell in enumerate(cells):
			if i not in self._cell_lengths:
				self._cell_lengths[i] = 0

			if self._cells_formatting:
				cell = self._cells_formatting(cell, i)

			cell = regex_match_cli_special_chars.sub("", str(cell))

			self._cell_lengths[i] = max(len(cell), self._cell_lengths[i])

		# max_lengths_length = len(self._col_pad_counts)
		# orig_str = str(cells)
		# stripped_str = regex_match_cli_special_chars.sub("", orig_str)
		#
		# val_len = len(stripped_str)
		#
		# if val_len < 1:
		# 	return
		#
		# if max_lengths_length > i:
		# 	orig_value = self._cell_max_lengths[i]
		# 	self._cell_max_lengths[i] = max(orig_value, val_len)
		# else:
		# 	self._cell_max_lengths.append(val_len)

	def render(self):
		res = ""

		for row_raw in self._rows_raw:
			sub_res = str(SimpleCliTableRow(
				*row_raw,
				cols_formatting=self._cells_formatting,
				col_pad_counts=self._cell_lengths,
			).render() + "\n")
			res += sub_res

		return res

	def __str__(self):
		return self.render()
