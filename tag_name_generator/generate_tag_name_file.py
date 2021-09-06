"""Opens a .yml localization file for country names and saves a
nested dictionary of matched names, tags and adjectives to .json."""
# Could potentially be automated in main program by checking game ver.
# Assumed to be compatible with other languages than English, untested.

# TO DO:
# 1. Proper comments.
# 2. Testing?

import json

from extract_localizations import extract_localizations
from match_localizations import match_localizations
from generator_logs import create_logs, compare_logs


def main():
    new_log, previous_log = create_logs()


    unpaired_adjectives, unpaired_names = (
        extract_localizations()
    )
    matched_names = (
        match_localizations(unpaired_adjectives, unpaired_names)
        )

    export_file = open("indices/names_and_tags.json", "w")
    json.dump(matched_names, export_file, indent=4)
    export_file.close()

    compare_logs(new_log, previous_log)

if __name__ == '__main__':
    main()