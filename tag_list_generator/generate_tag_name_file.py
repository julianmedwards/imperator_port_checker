"""Opens a .yml localization file for country names and saves a
nested dictionary of matched names, tags and adjectives to .json."""
# Could potentially be automated in main program by checking game ver.
# Assumed to be compatible with other languages than English, untested.

# TO DO:
# 1. Allow user to select localization file manually.
# 2. Log directory is selected automatically based on file location.
# 3. Proper comments.
# 4. Testing? example: Test all system localizations for logging.
# 5. Could make file and log names tied to selected game ver./mod.

# FIX ISSUE: previous_log is only for that date. Need to check for the actual
# last log made regardless of its from the current date.


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