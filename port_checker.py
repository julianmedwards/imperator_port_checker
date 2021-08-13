# game/setup/provinces

from select_save import select_save
from select_nation import select_nation
from find_nation import find_nation
from return_ports import return_ports

from classes.save import Save

# Look into re library. Regular Expressions, re.compile for checking for stuff?
# Increased save search efficiency?

# New way of calling functions and passing along has broken program
# response to entering an unrecognized nation name.

save_directory, save_name = select_save()   

current_save = Save(save_name, save_directory)

select_nation()

# nation, nation_tag, nation_found = find_nation()

# if nation_found == True:
#         return_ports(nation, nation_tag)
# else:
#     print("Please try again.")