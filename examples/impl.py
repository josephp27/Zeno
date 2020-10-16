import yaml

from ZenoMapper.Configuration import ConfigParser, Configuration
from ZenoMapper.Types import String, Boolean, Integer, List


class MyConfig(ConfigParser):
    """
    loading your own config is done via subclassing the ConfigParser class and implementing the
    get_config function.
    """

    def get_config(self):
        with open("examples/data.yml", 'r') as stream:
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


print(Spring().Data.myList)  # ['first', 'second', 'third']
print(Spring().Data.MongoDb.encryption is True)  # True
print(MyServer().host)  # my.server.com
