def select_save():
    """Prompt user for save name and location."""

    select_prompt = "Please enter the path to your save file: "
    save_directory = input(select_prompt)
    save_name = save_directory
    save_name = save_name.rsplit("\\")
    save_name = save_name[-1]
    return save_directory, save_name