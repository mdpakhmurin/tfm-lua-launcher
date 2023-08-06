from typing import List

from Protocols import ICommandLineHandler


class BaseHandlersChain:
    def __init__(self) -> None:
        self.handlers: List[ICommandLineHandler] = []

    def handle(self, args: List[str]) -> bool:
        for handler in self.handlers:
            is_break = handler.handle(args)
            if is_break:
                return True

        return False

    def register(self, commandHandler: ICommandLineHandler) -> None:
        self.handlers.append(commandHandler)
