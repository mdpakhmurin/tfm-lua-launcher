from typing import Protocol
from ICommandLineHandler import ICommandLineHandler
from typing import List


class ICommandLineHandlerChain(ICommandLineHandler, Protocol):
    def register(self, commandHandler: ICommandLineHandler) -> None:
        pass
