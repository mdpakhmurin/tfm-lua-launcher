from typing import Protocol
from Protocols.IBundle import IBundle

class IBundler(Protocol):
    def bundle(self, dir_path: str) -> IBundle: # type: ignore
        pass