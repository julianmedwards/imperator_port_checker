class Nation:
    """Class holding all required save info and indexing on a selected nation."""

    def __init__(
        self, save_directory, nation_name="", tag_index="", nation_tag="", 
        port_index="", ports=""):
        """Initialize basic nation indexes and attributes."""
        self.save_directory = save_directory

