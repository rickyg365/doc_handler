import os

from dataclasses import dataclass


# Base Class
class DocumentCreator:
    def __init__(self, dictionary_scripts=None, width=52):
        if dictionary_scripts is None:
            dictionary_scripts = {}

        self.scripts = dictionary_scripts
        self.max_width = width

    def extract(self):
        pass


class TxtCreator(DocumentCreator):
    def __init__(self, dictionary_scripts=None, width=52):
        super().__init__(dictionary_scripts, width)

    def fmt_script_list(self, title, script_list):
        # Title
        parsed = f"\n[  {title}  ]:\n"

        # Body
        for script in script_list:
            parsed += f"\n - {script}"

        # Separator
        parsed += f"\n\n{'_' * self.max_width}\n"

        return parsed

    def extract(self):
        new_doc = "\n--- INSERT NEW SCRIPTS HERE ---\n"

        # parse python and bash list
        for title, s_list in self.scripts.items():
            new_doc += self.fmt_script_list(s_list, title)

        return new_doc


class ReadmeCreator(DocumentCreator):
    def __init__(self, dictionary_scripts=None, width=52):
        super().__init__(dictionary_scripts, width)

    def fmt_script_list(self, title, script_list):
        # Title
        parsed = f"\n[  {title}  ]:\n"

        # Body
        for script in script_list:
            parsed += f"\n - {script}"

        # Separator
        parsed += f"\n\n{'_' * self.max_width}\n"

        return parsed

    def extract(self):
        new_doc = "\n--- INSERT NEW SCRIPTS HERE ---\n"

        # parse python and bash list
        for title, s_list in self.scripts.items():
            new_doc += self.fmt_script_list(s_list, title)

        return new_doc


if __name__ == "__main__":
    # key_name: ScriptType, key_value: List[Script]
    sample_input = {
        "PYTHON": ["script_obj1", "script_obj2"],
        "BASH": ["script_obj1", "script_obj2"]
    }

    # Create Handler
    new_handler = DocumentHandler(sample_input)

    #
    new_txt = new_handler.extract_txt()
    new_md = new_handler.extract_readme()

    #

    ...
