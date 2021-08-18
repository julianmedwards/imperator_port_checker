import json


def retrieve_nation_info(nation_name: str=""):

    with open("indices/names_and_tags.json") as json_file:
        nations = json.load(json_file)
    json_file.close()

    nation_found = False

    for key in nations:
        if nation_name.lower() in key["name"]:
            nation_found = True
            nation_name = key["nation_name"]
            nation_tag = key["tag"]
            nation_adjective = key["adjective"]

            print(nation_name)
            print(nations[nation_tag]["name"])

    if nation_found:
        return nation_name, nation_tag, nation_adjective
    else:
        print("Nation not found.")


def select_nation():
    """Takes user input to select the nation to find info for,
    cross-checking with game nation files."""

    select_prompt = "Enter the name of the nation you'd like to examine: "
    nation_name = input(select_prompt)
    
    nation_name, nation_tag, nation_adjective = (
        retrieve_nation_info(nation_name)
        )
    
