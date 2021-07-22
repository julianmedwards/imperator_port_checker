import json

def select_nation():
    """Takes user input to select the nation to find info for,
    cross-checking with game nation files."""

    with open("indices/names_and_tags.json") as json_file:
        countries = json.load(json_file)
    json_file.close()

    select_prompt = "Enter the name of the nation you'd like to examine: "
    nation_name = input(select_prompt)
    
    if nation_name in countries:
        return nation_name
    
    else:
        print("Nation not found.")
        return(select_nation())