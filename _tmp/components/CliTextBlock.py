from simputils.cli.components.CliFormatter import CliFormatter
from simputils.cli.enums.AnsiBackgroundColor import AnsiBackgroundColor
from simputils.cli.enums.AnsiForegroundColor import AnsiForegroundColor
from simputils.cli.enums.AnsiFormatting import AnsiFormatting


class CliTextBlock(CliFormatter):

	text: str = None

	def __init__(
		self,
		text: str = "",
		*,
		bg_color: AnsiBackgroundColor | int = None,
		fg_color: AnsiForegroundColor | int = None,
		formatting: AnsiFormatting | int = None,
		padding_prefix: int = 0,
		padding_suffix: int = 0,
		padding_prefix_symbol: str = " ",
		padding_suffix_symbol: str = " ",
	):
		self.text = text
		super().__init__(
			bg_color=bg_color,
			fg_color=fg_color,
			formatting=formatting,
			padding_prefix=padding_prefix,
			padding_suffix=padding_suffix,
			padding_prefix_symbol=padding_prefix_symbol,
			padding_suffix_symbol=padding_suffix_symbol,
		)

	def __str__(self):
		return self._wrapped(self.text)

	def __repr__(self):
		return str(self)
