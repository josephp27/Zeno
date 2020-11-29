import types
from abc import abstractmethod

from six import with_metaclass

from ZenoMapper.Types import ConfigTypes
from ZenoMapper.helpers import merge_dictionaries, traverse_dictionary, convert_section_to_keys


class ConfigParser(object):
    """The user inherits from this class, overloads get_config and returns a dictionary object"""

    @staticmethod
    @abstractmethod
    def get_config():
        """method to instantiate. must return a dictionary object"""
        pass


def get_settings():
    """function to get settings from the user inherited subclass ConfigParser"""
    subclasses = ConfigParser.__subclasses__()

    if len(subclasses) != 1:
        raise Exception("Only one class can subclass Configure got: " + ', '.join([cls.__name__ for cls in subclasses]))

    return subclasses[0].get_config()


class ConfigurationBase(type):
    """Configuration decorator to object map configuration files"""

    def __call__(cls, *args, **kwargs):
        """Called when the child class is instantiated"""
        obj = type.__call__(cls)

        super_class = kwargs.get('super_class', [])

        all_dictionaries = cls.populate(obj, super_class)
        # update the object (dict) with all the dictionaries found
        obj.update(all_dictionaries)
        return obj

    def __init__(cls, name, module=None, variables=None):
        """
        Required Args:
            cls (string) - The subclass of this
            module (string) - The project or module to be used
            variables (dict) - The variables in the class

        Optional Args:
            module (str) - The name of the module to be used for config lookups
        """
        cls.cls = name
        cls.module = module
        cls.variables = variables
        super(ConfigurationBase, cls).__init__(name)

    def populate(cls, obj, super_class=[]):
        """Method called to populate all member variables

        Required Args:
            cls (class) - The class this is decorated

        Optional Args:
            module (str) - The name of the module to be used for config lookups
        """
        variables = obj.variables

        # optionally specified section in the configured class.
        __section__ = variables.get('__section__', None)

        if __section__:
            lookup_keys = convert_section_to_keys(__section__)
        else:
            lookup_keys = super_class + [obj.cls]

        # all variables and functions found
        config_variables = []
        nested_classes = []

        # iterate through all member variables of class.
        nested_dictionaries = {}
        for name, value in variables.items():

            # recursing adds values like dict that throw errors when trying to access
            try:
                getattr(obj, name)
            except Exception:
                continue

            if isinstance(value, types.FunctionType):
                raise ReferenceError('Unexpected variable is not a class or variable: {}, {}'.format(name, value))

            is_callable = callable(getattr(obj, name, None))
            is_user_defined = not name.startswith('__')

            # if it is a variable created by the user, add it to the list of known config variables
            if (not is_callable and is_user_defined) or (is_callable and issubclass(value, ConfigTypes)):
                config_variables.append(name)

            # if it is a nested class, create another configuration object
            elif is_callable and is_user_defined:
                # we want to instantiate it so the user doesnt have to, i.e. the __call__()
                config_object = ConfigurationBase(name, cls.module, dict(variables[name].__dict__))
                config_object = config_object.__call__(super_class=lookup_keys)
                nested_dictionaries[name] = config_object
                nested_classes.append((name, config_object))

        variables_dictionary = {}
        # this is down here, because config makes multiple api calls, so doing it all at once saves precious
        # networking calls
        if config_variables:
            config = get_settings()

            for var in config_variables:
                # set the attribute of the member variable found in the config lookup
                # traverse the dictionary using list of lookup keys
                config_var = traverse_dictionary(config, lookup_keys)[var]

                # get the user defined type None, String, Integer, List, etc and convert it
                type_ = getattr(obj, var)
                converted_var = type_.convert(config_var) if type_ is not None else config_var

                variables_dictionary[var] = converted_var

        # merge all the dictionaries found together
        return merge_dictionaries(nested_dictionaries, variables_dictionary)


class Configuration(with_metaclass(ConfigurationBase, dict)):
    """
    Base class that all config classes should inherit from. Sets the metaclass
    """

    def __getattribute__(self, item):
        """if the value has been found, return it when trying to access said value
        since this is really just a fancy dictionary under the hood, we dont want to set the class variables
        because that would change it for every instance of the class.
        """
        if item in self:
            return self[item]

        return object.__getattribute__(self, item)

    # Configuration classes are dictionary object hybrids, so we need to handle both
    # variable assignment and key assignment
    def __setitem__(self, key, value):
        """Raise an exception. This is an immutable type."""
        raise AttributeError('{0} is an immutable object.'.format(self.__class__.__name__))

    def __setattr__(self, key, value):
        """Raise an exception. This is an immutable type."""
        raise AttributeError('{0} is an immutable object.'.format(self.__class__.__name__))
