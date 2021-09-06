"""Opens a .yml localization file and creates a .json file with matched
names, tags and adjectives in nested dictionaries."""

import re

def extract_localizations():
    countries_adjectives, countries_names = extract_countries()
    formables_adjectives, formables_names = extract_formables()

    return (countries_adjectives, countries_names,
            formables_adjectives, formables_names)


def extract_countries():
    countries_file = open(
    "game_files/countries_l_english.yml", "r", encoding="utf-8-sig"
    )
    countries_adjectives = {}
    countries_names = {}

    for line in countries_file:
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
                countries_adjectives.update({
                    f"{tag_or_adj}": {"adjective": name}
                    })
                
            else:
                countries_names.update({
                    f"{tag_or_adj}": {"name": name, "tag": tag_or_adj}
                    })
    countries_file.close()

    return countries_adjectives, countries_names


def extract_formables():
    formables_file = open(
        "game_files/nation_formation_l_english.yml", "r", encoding="utf-8-sig"
    )
    formables_adjectives = {}
    formables_names = {}
    
    for line in formables_file:
        line = str(line)
        if (line.startswith(" #") == False and
            line.startswith("\n") == False and
            re.search("_NAME", line) or
            re.search("_ADJ", line) or
            len(line.split(":")[0]) == 3
            ):
            tag_or_adj = re.split("\s|:", line)[1].lower()
            name = line.rsplit('"')[-2].lower()

            if  (re.search("adjective", tag_or_adj) or
                re.search("adj", tag_or_adj)
                ):
                formables_adjectives.update({
                    f"{tag_or_adj}": {"adjective": name}
                    })
                
            else:
                formables_names.update({
                    f"{tag_or_adj}": {"name": name, "tag": tag_or_adj}
                    })
    formables_file.close()

    return countries_adjectives, countries_names