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

# $THESSALY_NAME$

import json
import re

names_file = open("game_files/countries_l_english.yml", "r", encoding='utf-8-sig')
export_file = open("indices/names_and_tags.json", "w")


def generate_tag_name_file():
    unpaired_adjectives = []
    unpaired_names = {}
    names_and_tags = {}

    for line in names_file:
        if (line.startswith('#') == False and
            line.startswith('\n') == False and
            line[1].isalpha()):

            tag_or_adj = re.split('\s|:', line)[1].lower()
            name = line.rsplit('"')[-2].lower()

            if  (re.search('adjective', tag_or_adj) or
                re.search('adj', tag_or_adj)):
                unpaired_adjectives.append(tag_or_adj)
                
            else:
                unpaired_names.update({
                    f'{tag_or_adj}': {'name': name, 'tag': tag_or_adj}
                    })

    for adjective in unpaired_adjectives:
        if re.search('magna_graecia_feudatory', adjective):
            tag = str(adjective).replace('_adjective', "_name")
            
            if tag in unpaired_names:
                name = unpaired_names[tag].get('name')
                tag = unpaired_names[tag].get('tag')
                names_and_tags.update({
                    f'{tag}': {'name': name, 'tag': tag, 'adjective': adjective}
                    })
            
            else:
                Exception("Unexpected Magna Graecia Feudatory.")

        # elif re.search('_adjective', adjective):
        #     str(adjective).replace('_adjective', "")

        # elif re.search('_adj', adjective):
        #     str(adjective).replace('_adj', "")




        # if re.search('empire', adjective):
        #     print(str(adjective).rsplit('_', 1)[0])
        # elif re.search('nova', adjective):
        #     print(str(adjective).rsplit('_', 1)[0])
        # elif re.search('feudatory', adjective):
        #     print(str(adjective).rsplit('_', 1)[0])

        # elif str(adjective).split('_', 1)[0] in unpaired_names.values():
        #     print('Reggy boi')


    json.dump(names_and_tags, export_file)

    names_file.close()
    export_file.close()

generate_tag_name_file()