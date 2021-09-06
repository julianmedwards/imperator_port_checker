"""Matches name/tag combos in a nested dictionary."""

import re
import logging

def match_localizations(unpaired_adjectives: dict, unpaired_names: dict):
    matched_names = {}

    for adjective in unpaired_adjectives.copy():
        if re.search("magna_graecia_feudatory", adjective):
            tag = str(adjective).replace("_adjective", "_name")
            
            if tag in unpaired_names:
                name = unpaired_names[tag]['name']
                tag = unpaired_names[tag]['tag']
                real_adjective = unpaired_adjectives[adjective]['adjective']
                
                matched_names.update({
                    f"{tag}": {
                        "name": name,
                        "tag": tag,
                        "adjective": real_adjective
                        }
                    })
                unpaired_names.pop(tag)
                unpaired_adjectives.pop(adjective)
                continue
            else:
                logging.info(
                    f"Unpaired Magna Graecia Feudatory adjective: '{adjective}'"
                    )
                continue

        # These empire names are for events to rename dynastically
        # named countries. Probably not enough to work with just this
        # but useful for saving the localized names regardless.
        # Can reference from save file's name for the country.
        if re.match("appadocian_empire", adjective):
            tag = "cappadocian_empire_namec"
            
            if tag in unpaired_names:
                name = unpaired_names[tag]['name']
                tag = unpaired_names[tag]['tag']
                real_adjective = unpaired_adjectives[adjective]['adjective']
                
                matched_names.update({
                    f"{tag}": {
                        "name": name,
                        "tag": tag,
                        "adjective": real_adjective
                        }
                    })
                unpaired_names.pop(tag)
                unpaired_adjectives.pop(adjective)
                continue
            else:
                logging.info(
                    "Unpaired Cappadocian Empire(C) type adjective: "
                    f"'{adjective}'"
                )
                continue

        if re.search("empire", adjective):
            tag = str(adjective).replace("_adjective", "_name")
            
            if tag in unpaired_names:
                name = unpaired_names[tag]['name']
                tag = unpaired_names[tag]['tag']
                real_adjective = unpaired_adjectives[adjective]['adjective']
                
                matched_names.update({
                    f"{tag}": {
                        "name": name,
                        "tag": tag,
                        "adjective": real_adjective
                        }
                    })
                unpaired_names.pop(tag)
                unpaired_adjectives.pop(adjective)
                continue
            else:
                logging.info(f"Unpaired empire type adjective: '{adjective}'")
                continue

        if re.search("_adjective", adjective):
            tag = str(adjective).replace("_adjective", "_name")
            
            if tag in unpaired_names:
                name = unpaired_names[tag]['name']
                tag = unpaired_names[tag]['tag']
                real_adjective = unpaired_adjectives[adjective]['adjective']
                
                matched_names.update({
                    f"{tag}": {
                        "name": name,
                        "tag": tag,
                        "adjective": real_adjective
                        }
                    })
                unpaired_names.pop(tag)
                unpaired_adjectives.pop(adjective)
                continue
            else:
                logging.info(
                    f"Unpaired _adjective type adjective: '{adjective}'"
                    )
                continue

        if re.search("_adj", adjective):
            tag = str(adjective).rsplit("_", 1)[0]
            
            if tag in unpaired_names:
                name = unpaired_names[tag]['name']
                tag = unpaired_names[tag]['tag']
                real_adjective = unpaired_adjectives[adjective]['adjective']
                
                matched_names.update({
                    f"{tag}": {
                        "name": name,
                        "tag": tag,
                        "adjective": real_adjective
                        }
                    })
                unpaired_names.pop(tag)
                unpaired_adjectives.pop(adjective)
                continue

            elif str(adjective).replace("_adj", "_name") in unpaired_names:
                tag = str(adjective).replace("_adj", "_name")
                name = unpaired_names[tag]['name']
                tag = unpaired_names[tag]['tag']
                real_adjective = unpaired_adjectives[adjective]['adjective']
                
                matched_names.update({
                    f"{tag}": {
                        "name": name,
                        "tag": tag,
                        "adjective": real_adjective
                        }
                    })
                unpaired_names.pop(tag)
                unpaired_adjectives.pop(adjective)
                continue
            else:
                logging.info(f"Unpaired _adj type adjective: '{adjective}'")
                continue

# Check out weird unpaired cases. Consider logging more.
# Pop items from unpaired dicts as they're paired.
# Add all remaining names/adjs at the end as dict items for themselves.

        else:
            logging.warning(f"Unexpected adjective format: '{adjective}'")
    
    for tag in unpaired_names:
        logging.info(f"Unpaired tag/name: '{tag}'")

    matched_names.update(unpaired_names)
    matched_names.update(unpaired_adjectives)
    
    return matched_names