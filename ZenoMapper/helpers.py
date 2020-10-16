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
