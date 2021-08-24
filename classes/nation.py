"""Each module should also have a docstring describing
what the classes in a module can be used for."""
import re


class Nation:
    """Class holding all required save info and indexing on a selected nation."""
    def __init__(
        self, save_directory, nation_name, nation_tag, nation_adjective):
        """Initialize basic nation indexes and attributes."""
        self.save_directory = save_directory
        self.nation_name = nation_name
        self.nation_tag = nation_tag
        self.nation_adjective = nation_adjective
        self.save_index = ""
        self.ports_index = ""
        self.port_ids = ""

    def find_port_ids(self):
        """Define."""

        def clean_port_ids(port_list):
            """Define."""
            if port_list.isnumeric(): return True
            else: return False

        save_file = open(self.save_directory, 'r')

        index = 0
        flag = 0
        for line in save_file:
            index += 1
            if re.search(f'tag="{self.nation_tag.upper()}"', line):
                flag = 1
                self.save_index = index

            if "ports={" in line and flag == 1:
                self.ports_index = index
                port_line = line.split()
                self.port_ids = list(filter(clean_port_ids, port_line))
                break

        save_file.close()
