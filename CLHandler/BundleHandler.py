from typing import List

import os

from Bundlers import BundlerV1


class BundleHandler:
    def handle(self, args: List[str]) -> bool:
        if len(args) <= 2:
            return False

        path_to_dir = "./"
        if len(args) > 2:
            path_to_dir = args[2]

        if args[1] == "bundle":
            bundler = BundlerV1()

            bundle = bundler.bundle(path_to_dir)
            with open(os.path.join(path_to_dir, "bundle.txt"), "w+") as f:
                f.write(bundle.get_source())

            return True

        return False
