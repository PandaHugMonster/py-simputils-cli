from simputils.cli.enums.AnsiBackgroundColor import AnsiBackgroundColor
from simputils.cli.enums.AnsiForegroundColor import AnsiForegroundColor
from simputils.cli.enums.AnsiFormatting import AnsiFormatting


class CliTextConfig:

	is_ansi: bool = True
	bg_color: AnsiBackgroundColor | int = None
	fg_color: AnsiForegroundColor | int = None
	formatting: AnsiFormatting | int = None
	prefix: str = ""
	suffix: str = ""

	def __init__(
		self,
		bg_color: AnsiBackgroundColor | int = None,
		fg_color: AnsiForegroundColor | int = None,
		formatting: AnsiFormatting | int = None,
		is_ansi: bool = True,
		prefix: str = "",
		suffix: str = "",
	):
		self.is_ansi = is_ansi
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.formatting = formatting
		self.prefix = prefix
		self.suffix = suffix

	def format(self, *text: str, is_ansi: bool = True):
		res_text = ""

		for item in text:
			res_text += f"{item}"

		if not is_ansi:
			return res_text

		bg_color = self.bg_color
		fg_color = self.fg_color
		formatting = self.formatting

		prefix = self.prefix
		suffix = self.suffix

		res = ""
		if bg_color is not None:
			res += f"\033[{bg_color}m"
		res += "\033["
		# Beginning

		is_formatting_set = False
		if formatting is not None:
			is_formatting_set = True
			res += f"{int(formatting)}"

		if fg_color is not None:
			res += ";" if is_formatting_set else ""
			res += f"{int(fg_color)}"
		res += f"m"

		res += f"{prefix}{res_text}{suffix}"
		# End
		res += f"\033[0m"
		return res

	def __call__(self, *text: str, is_ansi: bool = True) -> str:
		return self.format(*text, is_ansi=is_ansi)
