from Launcher import WindowsLauncher
from Bundle import Bundle
from Bundler import Bundler

import sys
import os
from colorama import Fore

launcher = WindowsLauncher()
bundler = Bundler()


def process_command_line(args):
    if len(args) <= 2:
        return

    path_to_dir = args[2] if len(args) > 2 else "./"

    if args[1] == "run":
        bundle = bundler.bundle(path_to_dir)
        launcher.launch(bundle)
    elif args[1] == "bundle":
        bundle = bundler.bundle(path_to_dir)
        with open(os.path.join(path_to_dir, "bundle.txt"), "w+") as f:
            f.write(bundle.get_source())


if __name__ == "__main__":
    try:
        process_command_line(sys.argv)
    except Exception as ex:
        print(f"{Fore.RED}{ex}{Fore.RESET}")
