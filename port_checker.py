# game/setup/provinces

from return_ports import return_ports
from find_nation import find_nation

# New way of calling functions and passing along has broken program
# response to entering an unrecognized nation name.

nation, nation_tag, nation_found = find_nation()

if nation_found == True:
        return_ports(nation, nation_tag)
else:
    print("Please try again.")