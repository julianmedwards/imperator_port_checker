# Needs to be rewritten to search and recognize entries from the games'
# nations files.

def find_nation():
    test_nations = {'Bosporan Kingdom': 'BPK', 'Rome': 'ROM', 'Scythia': 'SCY'}

    nation_input = "Which nation's ports would you like to check? "
    nation = input(nation_input)

    if nation in test_nations:
        nation_tag = f'tag="{test_nations[nation]}"'
        print(nation_tag)
        nation_found = True
        return nation, nation_tag, nation_found
    else:
        print('Nation not found.')
        nation_found = False
        return nation_found