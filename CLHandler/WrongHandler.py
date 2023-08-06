from typing import List

from colorama import Fore


class WrongHandler:
    def handle(self, args: List[str]) -> bool:
        print(
            f'{Fore.RED}Wrong command. Write {Fore.BLUE}"help"{Fore.RED} to view the commands{Fore.RESET}'
        )
        return False
