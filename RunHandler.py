from typing import List

from Bundler import Bundler
from Launcher import WindowsLauncher


class RunHandler:
    def handle(self, args: List[str]) -> bool:
        if len(args) <= 2:
            return False

        path_to_dir = "./"
        if len(args) > 2:
            path_to_dir = args[2]

        if args[1] == "run":
            bundler = Bundler()
            launcher = WindowsLauncher()

            bundle = bundler.bundle(path_to_dir)
            launcher.launch(bundle)
            return True

        return False
