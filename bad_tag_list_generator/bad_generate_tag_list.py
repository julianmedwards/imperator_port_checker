"""Opens the game's countries file and turns it into an easily usable
list of all tags and their clean nation names."""
# Note - Could potentially be automated in main program by checking game ver.

import json

countries = open("game_files/countries.txt", "r", encoding='utf-8-sig')
export_file = open("indices/bad_names_and_tags.json", "w")


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