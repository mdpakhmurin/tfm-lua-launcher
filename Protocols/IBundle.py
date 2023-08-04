from typing import Protocol

class IBundle(Protocol):
    def get_source(self) -> str:
        pass