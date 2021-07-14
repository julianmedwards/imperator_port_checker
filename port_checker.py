# game/setup/provinces

    # csv import
# with open("data_files/steam_game_names.csv", 'r') as games_raw:
#     rows = csv.reader(games_raw, delimiter = ',')
#     games_list = []

#     for r in rows:
#         games_list.append(''.join(r))
#     print(games_list[0 : 14])

save_file = open("example_saves/451.2.2_bosporan_kingdom.rome", 'r')

# Needs to be rewritten to search and recognize entries from the games'
# nations files.
test_nations = {'Bosporan Kingdom': 'BPK', 'Rome': 'ROM', 'Scythia': 'SCY'}

nation_input = "Which nation's ports would you like to check? "
nation = input(nation_input)

if nation in test_nations:
    save_tag = f'tag="{test_nations[nation]}"'
    print(save_tag)
else:
    print('Nation not found.')

flag = 0
index = 0

for line in save_file:
    index += 1
    
    if save_tag in line:
        flag = 1
        save_nation_line = index
        print(save_nation_line)
    if flag == 1 and "ports={" in line:
        save_ports_line = index
        print(save_ports_line)

        # Find space, skip space, read every digit until hitting and
        # skipping another space, and so on, until reaching end bracket.

        break

if flag == 0:
    print('\nTag for', nation, 'not found')
else:
    print('\nTag for', nation, 'found in line:', save_nation_line)

save_file.close()