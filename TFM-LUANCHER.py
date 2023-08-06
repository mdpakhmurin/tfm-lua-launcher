from colorama import Fore
import sys

from DefaultHandlerChain import DefaultHandlerChain


def process_command_line(args):
    DefaultHandlerChain().handle(args)


if __name__ == "__main__":
    try:
        process_command_line(sys.argv)
    except Exception as ex:
        print(f"{Fore.RED}{ex}{Fore.RESET}")
