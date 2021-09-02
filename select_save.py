def select_save():
    """Prompt user for save name and location."""

    select_prompt = "Please enter the path to your save file: "
    save_directory = input(select_prompt)
    # For testing only
    if save_directory == "Test":
        save_directory = "C:\\Users\\Julia\\Documents\\Programming\\Repositories\\imperator_port_checker\\example_saves\\450.10.1_bosporan_kingdom.rome"
    if save_directory == "DynTest":
        save_directory = "C:\\Users\\Julia\\Documents\\Programming\\Repositories\\imperator_port_checker\\example_saves\\452.4.4 - Achaemenid Empire.rome"
    
    save_name = save_directory
    save_name = save_name.rsplit("\\")
    save_name = save_name[-1]

    return save_directory, save_name