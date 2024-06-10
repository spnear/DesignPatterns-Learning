from component import Text


class PlainText(Text):

    def __init__(self, text) -> None:
        self._text = text


    def render(self):
        return self._text