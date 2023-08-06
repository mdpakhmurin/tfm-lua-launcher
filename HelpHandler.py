from typing import List

from colorama import Fore


class HelpHandler:
    def handle(self, args: List[str]) -> bool:
        if len(args) < 2 or args[1] != "help":
            return False

        print(
            f"• Run project in transformice:{Fore.BLUE}run [path_to_directory]{Fore.RESET}\n"
            f"• Bundle project (bundle.txt will be created): {Fore.BLUE}bundle [path_to_directory]{Fore.RESET}",
        )

        return True
