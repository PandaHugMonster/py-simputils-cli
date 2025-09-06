#!/bin/env python3
from simputils.cli.components.CliTextBlock import CliTextBlock
from simputils.cli.components.SimpleCliTable import SimpleCliTable
from simputils.cli.components.SimpleCliTableRow import SimpleCliTableRow
from simputils.cli.enums.AnsiForegroundColor import AnsiForegroundColor
from simputils.cli.enums.AnsiFormatting import AnsiFormatting


def colouring(val: str | int | float, pos: int):
	if pos == 0 and isinstance(val, int | float):
		return CliTextBlock(f"{val}. ", fg_color=AnsiForegroundColor.CYAN)
	if pos == 1:
		return CliTextBlock(val, formatting=AnsiFormatting.BOLD)

	if isinstance(val, int | float):
		if val == 0:
			return CliTextBlock(val, fg_color=AnsiForegroundColor.GRAY)
		elif val > 0:
			return CliTextBlock(val, fg_color=AnsiForegroundColor.BLUE)
		elif val < 0:
			return CliTextBlock(val, fg_color=AnsiForegroundColor.RED)

	if isinstance(val, str) and "$" in val:
		val = float(val.replace("$", ""))
		if val > 0:
			return CliTextBlock(f"{val} $", fg_color=AnsiForegroundColor.GREEN)
		elif val < 0:
			return CliTextBlock(f"{val} $", fg_color=AnsiForegroundColor.RED)

	return CliTextBlock(val)


if __name__ == "__main__":

	table = SimpleCliTable(
		cells_formatting=colouring,
	)

	table.add_row(1, "Ivan Ponomarev", 35, 5, "900.01$")
	table.add_row(2, "Ivan Ponomarev", -50, 0, "-900.01 $", "L", "O", "Hello Panda")
	table.add_row(3, "Ivan Ponomarev", 500, 5, "101010 $")
	table.add_row(50000000000000000, "~", "~", None, "~", "~")
	table.add_row("Name:", "Ivan")
	table.add_row(CliTextBlock("Surname:", fg_color=AnsiForegroundColor.RED, prefix="> "), "Ponomarev")
	table.add_row("Nickname:", "PandaHugMonster", "", "POC", "", "", "", "Test")
	table.add_row("Age:", 35)

	print(f"{table}")

	# table.add_mutator(iter_callback)
	#
	# for i in range(1000, 1020):
	# 	table.add_row("Sheep {i}:", "🐃 {i}", data={"i": i})
	#
	# print(table)
