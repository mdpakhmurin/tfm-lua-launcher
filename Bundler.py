from Protocols.IBundle import IBundle
from Bundle import Bundle

import re
import os


class Bundler:
    def bundle(self, dir_path: str) -> IBundle:
        main_file_path = os.path.join(dir_path, "main.lua")
        if not os.path.isfile(main_file_path):
            raise FileNotFoundError(
                f"Not found main.lua file in the directory {main_file_path}"
            )

        source_code = self._process_file(main_file_path)

        bundle = Bundle()
        bundle.set_source(source_code)

        return bundle

    def _process_file(self, entry_point_path: str) -> str:
        file_content = self._read_file(entry_point_path)
        file_content = self._replace_dofiles(
            file_content, os.path.dirname(entry_point_path)
        )

        return file_content

    def _replace_dofiles(self, file_content: str, dir_path: str) -> str:
        """
        This function replaces all occurrences of `dofile` in the given file content
        with the content of the file specified in the `dofile` call. This replacement
        is done recursively, meaning that if the replacement text itself
        contains `dofile` calls, those will also be replaced.
        """

        # Searches for lines starting with dofile('...') or dofile("..."),
        # where there are no -- characters before dofile() on the same line
        search_pattern = r'(?m)^(?!.*--)dofile\(([\'"])(.+?)\1\)'
        replace_pattern = r"(?m)^(?!.*--)dofile\({quote_char}{file_path}{quote_char}\)"

        dofiles_matches = re.findall(search_pattern, file_content)
        for match in dofiles_matches:
            quote_char, dofile_path = match

            full_file_path = os.path.join(dir_path, dofile_path)
            replacement_text = self._process_file(full_file_path)

            file_content = re.sub(
                replace_pattern.format(quote_char=quote_char, file_path=dofile_path),
                replacement_text,
                file_content,
            )
        return file_content

    def _read_file(self, filepath: str) -> str:
        with open(filepath, "r") as f:
            return f.read()
