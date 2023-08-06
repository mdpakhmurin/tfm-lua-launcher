from colorama import Fore
import sys

from DefaultHandlersChain import DefaultHandlersChain


def process_command_line(args):
    DefaultHandlersChain().handle(args)


if __name__ == "__main__":
    try:
        process_command_line(sys.argv)
    except Exception as ex:
        print(f"{Fore.RED}{ex}{Fore.RESET}")
