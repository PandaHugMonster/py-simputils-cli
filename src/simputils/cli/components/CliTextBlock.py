from typing import AnyStr

from typing_extensions import Any

from simputils.cli.components.CliTextConfig import CliTextConfig


class CliTextBlock(CliTextConfig):
	text: list[Any] = None

	def __init__(
		self,
		*text: Any,
		**kwargs
	):
		self.text = list(text)
		super().__init__(**kwargs)

	def __str__(self):
		return self.format(is_ansi=self.is_ansi)

	def format(self, *text: str, is_ansi: bool = True) -> str:
		text = text if text else self.text
		return super().format(*text, is_ansi=is_ansi)
