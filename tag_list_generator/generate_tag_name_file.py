"""Opens a .yml localization file for country names and saves a
nested dictionary of matched names, tags and adjectives to .json."""
# Could potentially be automated in main program by checking game ver.
# Assumed to be compatible with other languages than English, untested.

# TO DO:
# 1. Create logging file and check whether unpaired entries are different
# between each log.
# 2. Allow user to select localization file manually.
# 3. Proper commenting.
# 4. Create human readable names_and_tags file output.

import json
import logging
from extract_localized_names import extract_localized_names
from match_tags_and_adjectives import match_tags_and_adjectives

logging.basicConfig(level=logging.INFO)

def generate_tag_name_file():
    unpaired_adjectives, unpaired_names = (
        extract_localized_names()
    )
    matched_names = (
        match_tags_and_adjectives(unpaired_adjectives, unpaired_names)
        )

    export_file = open("indices/names_and_tags.json", "w")
    json.dump(matched_names, export_file)
    export_file.close()


generate_tag_name_file()