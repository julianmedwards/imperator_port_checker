"""Opens the game's English localized country names file and returns a clean 
dictionary of tags and names saved in a .json file."""
# Note - Could potentially be automated in main program by checking game ver.
# Should be compatible with other language files, tags *should* be same.

# YAML file iteration procedure:
# Four Name Types:
# 1. Non-Country Entities (Rebels, unlanded Barbs, Mercenaries etc.) Only 3.
# 2. Settled spawned barbarian tribes, full name.
# 3. Tag + Tag_ADJ, normal.
# 4. Roman civil war tags.
# 5. Rename events (formed Empires)
# 6. A bunch of random other shit that isn't just using a 3 letter tag
#    including _NAME.
# 7. SEL_DYN, MRY_DYN, PRY_DYN - Dynamically named countries. Oof.

# All of these have in common that they are separated by the a colon
# with 0 or 1 and the name in quotes. (Means nothing to us.)
# Go through each line regardless of what it is and store it cleaned up.
# Only issue is pairing names and ADJs in the dictionary.
# Next question: Does every name have an adjective? Answer: No. Blank.

import json
import re

names_file = open("game_files/countries_l_english.yml", "r", encoding='utf-8-sig')
export_file = open("indices/names_and_tags.json", "w")


def generate_tag_name_file():
    unpaired_adjectives = []
    unpaired_names = {}
    names_and_tags = {}

    for line in names_file:
        # if (line.startswith(' #') == False and
        # line.startswith('#') == False and
        # line.startswith(' \n') == False and
        # line.startswith('\n') == False and
        # line.startswith('\ufeffl_english') == False):

        if (line.startswith('#') == False and
            line.startswith('\n') == False and
            line[1].isalpha()):
            tag_or_adj = re.split('\s|:', line)[1]
            name = line.rsplit('"')[-2]
            if tag_or_adj.endswith("ADJ") or tag_or_adj.endswith("ADJECTIVE"):
                unpaired_adjectives.append(tag_or_adj)
            else:
                unpaired_names.update({name: tag_or_adj})

    for adjective in unpaired_adjectives:
        adjective = adjective.rsplit('_', 1)[0]
        if adjective in unpaired_names:
            print("we got one boss")


    json.dump(names_and_tags, export_file)

    names_file.close()
    export_file.close()

generate_tag_name_file()