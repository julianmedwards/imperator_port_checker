def select_nation():
    """Takes user input to select the nation to find info for,
    cross-checking with game nation files."""

    select_prompt = "Enter the name of the nation you'd like to examine: "
    nation_name = input(select_prompt)
    
    countries = open("indices/tags_and_names.txt", "r")
    for line in countries:
            

        countries.close()
        return nation_name