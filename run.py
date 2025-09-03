#!/bin/env python3
from simputils.cli.components.CliTextBlock import CliTextBlock
from simputils.cli.components.CliTextConfig import CliTextConfig
from simputils.cli.components.SimpleCliTable import SimpleCliTable
from simputils.cli.components.SimpleCliTableRow import SimpleCliTableRow
from simputils.cli.enums.AnsiForegroundColor import AnsiForegroundColor
from simputils.cli.enums.AnsiFormatting import AnsiFormatting


def iter_callback(row: SimpleCliTableRow) -> tuple[SimpleCliTableRow | str] | tuple[str, SimpleCliTableRow]:
	return "TEST", row


if __name__ == "__main__":

	def _if_number(val: str | int | float):
		if isinstance(val, bool):
			return CliTextBlock(val, fg_color=AnsiForegroundColor.BLUE if val else AnsiForegroundColor.RED, prefix="B:")
		elif isinstance(val, int | float):
			if val == 0:
				return CliTextBlock(val, fg_color=AnsiForegroundColor.BROWN, prefix="N:")
			elif val > 0:
				return CliTextBlock(val, fg_color=AnsiForegroundColor.GREEN, prefix="N:")
			elif val < 0:
				return CliTextBlock(val, fg_color=AnsiForegroundColor.RED, prefix="N:")

		elif isinstance(val, list | tuple):
			return CliTextBlock(val, fg_color=AnsiForegroundColor.PURPLE, prefix="I:")
		elif isinstance(val, dict):
			return CliTextBlock(val, fg_color=AnsiForegroundColor.CYAN, prefix="D:")
		elif val is None:
			return CliTextBlock("None", fg_color=AnsiForegroundColor.GRAY, prefix="{{", suffix="}}")

		return CliTextBlock(val, formatting=AnsiFormatting.BOLD, prefix="T:")

	row = SimpleCliTableRow(
		True, False, 1, 0, -2, 0.5, None, "", "Text 1", [1, 2, 3], {"1": 1, "2": 2, "3": 3},
		# "test 1", bool("123456789123456789"), "test 3",

		col_pad_counts={0: 10, 1: 15},
		cols_formatting=_if_number,
		# cols_formatting={1: _if_number},
		# cols_formatting={1: CliTextConfig(fg_color=AnsiForegroundColor.GREEN, prefix="{{", suffix="}}")},
		border_vertical_char="|",
		# content_pad_char="%",
		#
		# padding_left_char="<",
		# padding_left_count=5,
		#
		# padding_right_char=">",
		# padding_right_count=5,
	)

	# print(f"{row.render([10,])}")
	print(f"{row.render()}")

	# table = SimpleCliTable(padding_right=3)
	# table.debug_paddings = True
	#
	# table.set_col_formatting(0, CliTextConfig(
	# 	fg_color=AnsiForegroundColor.BLUE,
	# 	prefix="#" + " " * 1,
	# ))
	# table.set_col_formatting(1, CliTextConfig(
	# 	fg_color=AnsiForegroundColor.CYAN,
	# ))
	#
	# table.add_row("Name:", "Ivan")
	# table.add_row(str(CliTextBlock("Surname:", fg_color=AnsiForegroundColor.RED, prefix="> ")), "Ponomarev")
	# table.add_row("Nickname:", "PandaHugMonster")
	# table.add_row("Age:", 35)
	#
	# table.add_mutator(iter_callback)
	#
	# for i in range(1000, 1020):
	# 	table.add_row("Sheep {i}:", "🐃 {i}", data={"i": i})
	#
	# print(table)
