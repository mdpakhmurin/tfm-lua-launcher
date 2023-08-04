from typing import Protocol
from IBundle import IBundle

class ILauncher(Protocol):
    def launch(self, bundle: IBundle):
        pass