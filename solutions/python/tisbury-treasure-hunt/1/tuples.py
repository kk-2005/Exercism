"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """
    return record[-1]
    pass


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """
    return (coordinate[0],coordinate[1])
    pass


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """
    rui_coordinate_string = "".join(rui_record[1])
    return azara_record[1] == rui_coordinate_string


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    tup1 = azara_record + rui_record 
    az_coord = convert_coordinate(tup1[1]) 
    rui_coord = tup1[3] 
    if az_coord == rui_coord: 
        return tup1 
    else: 
        return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records. Parameters: combined_record_group (tuple): Everything from both participants. Returns: str: Everything "cleaned", excess coordinates and information are removed. """
    format_string = ""

    for c in combined_record_group:
        c_tup = (c[0],) + c[2:]
        format_string += f"{c_tup}\n"

    return format_string
