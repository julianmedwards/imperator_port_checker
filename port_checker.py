# game/setup/provinces

from return_ports import return_ports
from find_nation import find_nation
from classes.save import Save

# New way of calling functions and passing along has broken program
# response to entering an unrecognized nation name.

current_save = Save()

save_directory, save_name = current_save.select_save()

# nation, nation_tag, nation_found = find_nation()

# if nation_found == True:
#         return_ports(nation, nation_tag)
# else:
#     print("Please try again.")