"""Opens the game's countries file and turns it into an easily usable
list of all tags and their clean nation names."""

countries = open("game_files/countries.txt", "r", encoding='utf-8-sig')

tags_and_names = open("indices/tags_and_names.txt", "w")

test_line = ""

for line in countries:
    if line.startswith("#") and line.endswith('.txt"\n'):
        line = line[1:4]
    elif line.endswith('.txt"\n'):
        line = line[:3]
    else:
        continue
    
    test_line = line
    tags_and_names.write(f"{line}\n")

countries.close()
tags_and_names.close()