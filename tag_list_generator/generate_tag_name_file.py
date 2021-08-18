"""Opens a .yml localization file for country names and saves a
nested dictionary of matched names, tags and adjectives to .json."""
# Could potentially be automated in main program by checking game ver.
# Assumed to be compatible with other languages than English, untested.

# TO DO:
# 1. Proper comments.
# 2. Testing?


import json
from extract_localized_names import extract_localized_names
from match_tags_and_adjectives import match_tags_and_adjectives
from generator_logs import create_logs, cross_reference_logs


def main():
    new_log, previous_log = create_logs()


    unpaired_adjectives, unpaired_names = (
        extract_localized_names()
    )
    matched_names = (
        match_tags_and_adjectives(unpaired_adjectives, unpaired_names)
        )

    export_file = open("indices/names_and_tags.json", "w")
    json.dump(matched_names, export_file, indent=4)
    export_file.close()

    cross_reference_logs(new_log, previous_log)

if __name__ == '__main__':
    main()