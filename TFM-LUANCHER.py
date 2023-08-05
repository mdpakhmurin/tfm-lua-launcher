from Launcher import WindowsLauncher
from Bundle import Bundle
from Bundler import Bundler

import sys

launcher = WindowsLauncher()
bundler = Bundler()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        path = "./"
        if len(sys.argv) > 2:
            path = sys.argv[2]
        bundle = bundler.bundle(path)
        launcher.launch(bundle)
