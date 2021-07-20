class Save:

    def __init__(self, save_name="", save_directory=""):
        """Initialize game save info."""
        self.save_name = save_name
        self.save_directory = save_directory

    def select_save(self):
        """Prompt user for save name and location."""
        select_prompt = "Please enter the path to your save file: "
        self.save_directory = input(select_prompt)
        self.save_name = self.save_directory
        self.save_name = self.save_name.rsplit("\\")
        self.save_name = self.save_name[-1]
        return self.save_directory, self.save_name