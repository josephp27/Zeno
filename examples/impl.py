from functools import lru_cache

import yaml

from ZenoMapper.Configuration import ConfigParser, Configuration
from ZenoMapper.Types import String, Boolean, Integer, List
from ZenoMapper.zeno import Zeno


class MyConfig(ConfigParser):
    """
    loading your own config is done via subclassing the ConfigParser class and implementing the
    get_config function.
    """

    @staticmethod
    @lru_cache(maxsize=None)  # @cache if you're on python3.9 or later
    def get_config():
        # each time an object is instantiated, this is called, so let's cache the results to increase performance
        with open("data.yml", 'r') as stream:
            return yaml.safe_load(stream)


class Spring(Configuration):
    """
    loads in from data.yml. accessing nested sections can be done via nested classes
    """

    class Data:
        class MongoDb:
            database = String()
            encryption = Boolean()  # conversion automatically happens when specifying the type
            encryptionKey = String()
            password = String()
            replicaSet = String()

        second = Integer()
        myList = List()


class MyServer(Configuration):
    host = String()
    port = Integer()


class SuperNested(Configuration):
    """Specifying section"""
    __section__ = 'Spring.Data.MongoDb'

    database = String()
    encryption = Boolean()
    encryptionKey = String()
    password = String()
    replicaSet = String()

    class Nested:
        key = Integer()


print(Spring().Data.myList)  # ['first', 'second', 'third']
print(Spring().Data.MongoDb.encryption is True)  # True
print(MyServer().host)  # my.server.com
print(SuperNested().database)  # TESTDB
print(SuperNested().Nested.key)  # True

# this method is used if specifying a class is not ideal for the user
zeno = Zeno()
print(zeno.Spring.Data.MongoDb.database)  # TESTDB

# if the constructor is specified, it denotes how to search withing the yml file starting
# in the section mongodb withing the data section, within the spring section
# in this case it will be all these member variables: database encryption encryptionKey password replicaSet
zeno_2 = Zeno('Spring.Data.MongoDb')
print(zeno_2.database)  # TESTDB
