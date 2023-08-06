from typing import List

from Bundlers import BundlerV1
from Launchers import WindowsLauncher


class RunHandler:
    def handle(self, args: List[str]) -> bool:
        if len(args) < 2:
            return False

        path_to_dir = "./"
        if len(args) > 2:
            path_to_dir = args[2]

        if args[1] == "run":
            bundler = BundlerV1()
            launcher = WindowsLauncher()

            bundle = bundler.bundle(path_to_dir)
            launcher.launch(bundle)
            return True

        return False
