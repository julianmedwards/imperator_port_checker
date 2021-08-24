"""Opens a .yml localization file and creates a .json file with matched
names, tags and adjectives in nested dictionaries."""

import re

def extract_localized_names():
    names_file = open(
    "game_files/countries_l_english.yml", "r", encoding="utf-8-sig"
    )
    unpaired_adjectives = {}
    unpaired_names = {}

    for line in names_file:
        line = str(line)
        if (line.startswith("#") == False and
            line.startswith("\n") == False and
            line[1].isalpha()
            ):
            tag_or_adj = re.split("\s|:", line)[1].lower()
            name = line.rsplit('"')[-2].lower()

            if  (re.search("adjective", tag_or_adj) or
                re.search("adj", tag_or_adj)
                ):
                unpaired_adjectives.update({
                    f"{tag_or_adj}": {"adjective": name}
                    })
                
            else:
                unpaired_names.update({
                    f"{tag_or_adj}": {"name": name, "tag": tag_or_adj}
                    })
    names_file.close()
    return unpaired_adjectives, unpaired_names