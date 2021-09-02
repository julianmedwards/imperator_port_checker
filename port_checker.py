"""Blay."""

# game/setup/provinces

from itertools import filterfalse
import os

from tag_name_generator.generate_tag_name_file import main as generate_file
from select_save import select_save
from select_nation import select_nation

from classes.save import Save
from classes.nation import Nation

# SET PYTHONPATH=C:\Users\Julia\Documents\Programming\Repositories\imperator_port_checker


# Look into re library. Regular Expressions, re.compile for checking for stuff?
# Increased save search efficiency?

# Tools for war after action reports, etc. Enter two saves, tell you demographic
# changes between saves etc.

def main():
    active = True
    while active:
        if not os.path.exists("indices/names_and_tags.json"):
            l1 = "Missing names and tags file needed to use port checker. "
            l2 = "Would you like to run the generator and create one? (Y/N) "
            run_generator_prompt =  (l1 + l2)
            response = input(run_generator_prompt)
            
            if response == "Y": generate_file()
            elif response == "N":
                print("Ending process.")
                active = False

        save_directory, save_name = select_save()
        current_save = Save(save_name, save_directory)

        selecting = True
        while selecting == True:
            selecting, nation_name, nation_tag, nation_adjective = (
                select_nation(selecting))
            if selecting:
                print("Nation not found, please try again.")
                continue

        current_nation = Nation(current_save.save_directory, nation_name,
                                nation_tag, nation_adjective)
        
        current_nation.find_port_ids()
        print(current_nation.port_ids)
        break

        


if __name__ == '__main__':
    main()