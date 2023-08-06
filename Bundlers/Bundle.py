class Bundle:
    def __init__(self) -> None:
        self._source = ''

    def get_source(self) -> str:
        return self._source

    def set_source(self, source: str) -> None:
        self._source = source