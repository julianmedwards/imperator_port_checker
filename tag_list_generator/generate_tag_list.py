"""Opens the game's English localized country names file and returns a clean 
dictionary of tags and names saved in a .json file."""
# Note - Could potentially be automated in main program by checking game ver.

import yaml
import json

countries = open("game_files/countries_I_english.yml", "r")
export_file = open("indices/names_and_tags.json", "w")

# YAML file iteration procedure:
# Go through each line. Only skip over any line that doesn't start with
# 3 letters and a colon or 3 letters, underscore, ADJ.


def generate_tag_name_file():
    names_and_tags = {}

    for line in countries:
        if line.startswith("#") and line.endswith('.txt"\n'):
            tag = line.lower()[1:4]
            name = line.rsplit(".", 1)
            name = name[0].rsplit("/")[-1].replace("_", " " )
            names_and_tags[name] = tag

        elif line.endswith('.txt"\n'):
            tag = line.lower()[:3]
            name = line.rsplit(".", 1)
            name = name[0].rsplit("/")[-1].replace("_", " " )
            names_and_tags[name] = tag

        else:
            continue

    json.dump(names_and_tags, export_file)

    countries.close()
    export_file.close()

generate_tag_name_file()