from abc import abstractmethod


class ConfigTypes(object):
    """
    Configuration Types base class. All subclasses must instantiate convert
    """

    @abstractmethod
    def convert(self, obj):
        """Method called to convert obj to it's class type, all values from consul come in as a string

        Required Args:
            obj (str) - The object to be converted

        returned:
            int - The object a derived class type
        """
        pass


class Integer(ConfigTypes):
    """
    Integer class to be used with Configuration class
    """

    def convert(self, obj):
        """Method called to convert obj to an integer

        Required Args:
            obj (str) - The object to be converted

        returned:
            int - The object as an integer
        """
        return int(obj)

    def __index__(self):
        """This function is used to trick pylint into thinking this is a valid integer"""
        pass


class List(ConfigTypes):
    """
    List class to be used with Configuration class
    """

    def convert(self, obj):
        """Method called to convert obj to a list

        Required Args:
            obj (str) - The comma separated object to be converted

        returned:
            list - The object as a list
        """
        if isinstance(obj, list):
            return obj

        if isinstance(obj, str):
            if not obj:
                return []

            if obj[0] == '[' and obj[-1] == ']':
                obj = obj[1:len(obj) - 1]

            if obj == '':
                # the user specified [] in their config
                return []

            obj = obj.split(',')
            return [item.strip() for item in obj]

        raise Exception('{} is not a string or list'.format(obj))

    def __getitem__(self, item):
        """This function is used to trick pylint into thinking this is a valid list"""
        pass


class Boolean(ConfigTypes):
    """
    Boolean class to convert input to True/False
    """

    def convert(self, obj):
        """Method called to convert obj to a boolean

        Required Args:
            obj (obj) - The object to be converted

        returned:
            int - The object as a True/False
        """
        if isinstance(obj, bool):
            return obj

        if not isinstance(obj, str):
            raise ValueError('Invalid literal for boolean. Not a string: {}'.format(obj))

        return obj.lower() in ('yes', 'true', 't', '1')


class String(ConfigTypes):
    """
    String class to be used with Configuration class
    """

    def convert(self, obj):
        """Method called to convert obj to a string
        NOTE: this is the same as ascii_normalize
            - ignores cyclical dependencies

        Required Args:
            obj (obj) - The object to be converted

        returned:
            int - The object as a ascii normalized string
        """
        try:
            return str(obj)
        except UnicodeEncodeError:
            return obj
