"""Yeet. yeet."""

import json


def retrieve_nation_localization(nation_name: str=""):
    """Blah."""
    with open("indices/names_and_tags.json") as json_file:
        nations = json.load(json_file)
    json_file.close()

    nation_found = False
    try:
        for key in nations:
            if nation_name.lower() in nations[key]["name"]:
                nation_found = True
                nation_name = nations[key]["name"]
                nation_tag = nations[key]["tag"]
                nation_adjective = nations[key]["adjective"]
                break
    except KeyError:
        nation_found = False

    if nation_found:
        return nation_found, nation_name, nation_tag, nation_adjective
    if not nation_found:
        nation_name = ""
        nation_tag = ""
        nation_adjective = ""
        return nation_found, nation_name, nation_tag, nation_adjective
    else:
        raise Exception("An unexpected error occured in finding your nation.")


def select_nation(selecting):
    """Takes user input to select the nation to find info for,
    cross-checking with game nation files."""

    select_prompt = "Enter the name of the nation you'd like to examine: "
    nation_name = input(select_prompt)
    
    nation_found, nation_name, nation_tag, nation_adjective = (
        retrieve_nation_localization(nation_name)
        )
    if nation_found:
        selecting = False

    return selecting, nation_name, nation_tag, nation_adjective
