from typing import Protocol
from typing import List


class ICommandLineHandler(Protocol):
    def handle(self, args: List[str]) -> bool:  # type: ignore
        """
        Handle command line arguments

        Returns:
            bool: true if handler wants to break chain, false otherwise.
        """
        pass
