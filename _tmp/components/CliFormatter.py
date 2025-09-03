from simputils.cli.enums.AnsiBackgroundColor import AnsiBackgroundColor
from simputils.cli.enums.AnsiForegroundColor import AnsiForegroundColor
from simputils.cli.enums.AnsiFormatting import AnsiFormatting


class CliFormatter:

	bg_color: AnsiBackgroundColor | int = None
	fg_color: AnsiForegroundColor | int = None
	formatting: AnsiFormatting | int = None
	padding_prefix_count: int = 0
	padding_prefix_symbol: str = " "
	padding_suffix_count: int = 0
	padding_suffix_symbol: str = " "

	def __init__(
		self,
		*,
		bg_color: AnsiBackgroundColor | int = None,
		fg_color: AnsiForegroundColor | int = None,
		formatting: AnsiFormatting | int = None,
		padding_prefix: int = 0,
		padding_suffix: int = 0,
		padding_prefix_symbol: str = " ",
		padding_suffix_symbol: str = " ",
	):
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.formatting = formatting
		self.padding_prefix_count = padding_prefix
		self.padding_suffix_count = padding_suffix
		self.padding_prefix_symbol = padding_prefix_symbol
		self.padding_suffix_symbol = padding_suffix_symbol

	def _wrapped(
		self,
		text: str,
		*,
		bg_color: AnsiBackgroundColor | int = None,
		fg_color: AnsiForegroundColor | int = None,
		formatting: AnsiFormatting | int = None,
		padding_prefix: int = None,
		padding_suffix: int = None,
		padding_prefix_symbol: str = None,
		padding_suffix_symbol: str = None,
	) -> str:

		bg_color = bg_color if bg_color is not None else self.bg_color
		fg_color = fg_color if fg_color is not None else self.fg_color
		formatting = formatting if formatting is not None else self.formatting
		padding_prefix = padding_prefix if padding_prefix is not None else self.padding_prefix_count
		padding_suffix = padding_suffix if padding_suffix is not None else self.padding_suffix_count
		padding_prefix_symbol = padding_prefix_symbol if padding_prefix_symbol is not None else self.padding_prefix_symbol
		padding_suffix_symbol = padding_suffix_symbol if padding_suffix_symbol is not None else self.padding_suffix_symbol

		res = ""
		if bg_color is not None:
			res += f"\033[{bg_color}m"
		res += "\033["
		# Beginning

		prefix = padding_prefix_symbol * padding_prefix
		suffix = padding_suffix_symbol * padding_suffix

		is_formatting_set = False
		if formatting is not None:
			is_formatting_set = True
			res += f"{int(formatting)}"

		if fg_color is not None:
			res += ";" if is_formatting_set else ""
			res += f"{int(fg_color)}"
		res += f"m"

		res += f"{prefix}{text}{suffix}"
		# End
		res += f"\033[0m"

		return res


	def __call__(
		self,
		text: str = "",
		*,
		bg_color: AnsiBackgroundColor | int = None,
		fg_color: AnsiForegroundColor | int = None,
		formatting: AnsiFormatting | int = None,
		padding_prefix: int = None,
		padding_suffix: int = None,
		padding_prefix_symbol: str = None,
		padding_suffix_symbol: str = None,
	):
		return self._wrapped(
			text,
			bg_color=bg_color,
			fg_color=fg_color,
			formatting=formatting,
			padding_prefix=padding_prefix,
			padding_suffix=padding_suffix,
			padding_prefix_symbol=padding_prefix_symbol,
			padding_suffix_symbol=padding_suffix_symbol,
		)
