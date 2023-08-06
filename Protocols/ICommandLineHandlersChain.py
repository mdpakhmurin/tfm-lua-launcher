from typing import Protocol
from Protocols import ICommandLineHandler
from typing import List


class ICommandLineHandlersChain(ICommandLineHandler, Protocol):
    def register(self, commandHandler: ICommandLineHandler) -> None:
        pass
