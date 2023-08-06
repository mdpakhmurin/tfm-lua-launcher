from typing import Protocol
from Protocols import IBundle


class ILauncher(Protocol):
    def launch(self, bundle: IBundle):
        pass
