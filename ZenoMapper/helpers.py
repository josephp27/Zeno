import re


def merge_dictionaries(base, primary):
    """
    :param base: dictionary to replace values with
    :param primary: dictionary whose values we care about most
    :return: merged dictionary
    """
    # create the dictionary if we pass a None
    base = base or {}
    primary = primary or {}

    merged = base.copy()
    merged.update(primary)
    return merged


def to_snake_case(section):
    """Transforms input to snake_case from formats like CamelCase

    Required Args:
        section (str) - Name of String to be converted

    Returns:
        (str) section in snake_case
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', section).lower()


def traverse_dictionary(dictionary, keys):
    """Searches dictionary for all keys in order

    Required Args:
        dictionary (dict) - Dictionary to be searched
        keys (list) - list of keys to be searched in order

    Returns:
        (dict) value
    """
    curr_dictionary = dictionary

    for key in keys:
        curr_dictionary = get_dict(curr_dictionary, key)

    return curr_dictionary


def get_dict(dictionary, key):
    """Attempts to get value from dictionary

    Required Args:
        dictionary (dict) - Dictionary to be searched
        keys (list) - list of keys to be searched in order

    Returns:
        (dict) value

    Raises:
        KeyError
    """
    try:
        # get the value as is
        return dictionary[key]
    except KeyError:
        pass

    try:
        # lower the value then try to get it
        return dictionary[key.lower()]
    except KeyError:
        pass

    # snake case it then try to get
    return dictionary[to_snake_case(key)]


def convert_section_to_keys(section):
    """Splits section into its keys to be searched in order

    Required Args:
        section (str) - Period delimited str

    Returns:
        (list) keys
    """
    return section.split('.')
