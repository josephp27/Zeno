from ZenoMapper import get_settings, traverse_dictionary, convert_section_to_keys


class Zeno(dict):
    """
    Zeno object to be used when not wanting to use inheritance based way
    """

    def __getattribute__(self, item):
        """if the value has been found, return it when trying to access said value"""
        if item in self:
            # if it is a dictionary return a zeno object, else return just the item
            return Zeno(self[item]) if isinstance(self[item], dict) else self[item]

        return object.__getattribute__(self, item)

    # Configuration classes are dictionary object hybrids, so we need to handle both
    # variable assignment and key assignment
    def __setitem__(self, key, value):
        """Raise an exception. This is an immutable type."""
        raise AttributeError('{0} is an immutable object.'.format(self.__class__.__name__))

    def __setattr__(self, key, value):
        """Raise an exception. This is an immutable type."""
        raise AttributeError('{0} is an immutable object.'.format(self.__class__.__name__))

    def __init__(self, section=''):
        """Method called to populate all member variables

        Required Args:
            cls (class) - The class this is decorated

        Optional Args:
            module (str) - The name of the module to be used for config lookups
        """
        if isinstance(section, str):
            # the user defined file we would like to get the data from
            config = get_settings()

            # convert the keys and lookup the dictionary
            lookup_keys = convert_section_to_keys(section)

            # traverse the dictionary using list of lookup keys
            searched_dictionary = traverse_dictionary(config, lookup_keys) if section else config
        else:
            # it is a dictionary and we don't want to do anything
            searched_dictionary = section

        super(Zeno, self).__init__(searched_dictionary)
