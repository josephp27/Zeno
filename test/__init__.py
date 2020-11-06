from ZenoMapper import String, Boolean, Integer, Configuration, List, ConfigParser

parsed_yml = {
    'Spring': {
        'Data': {
            'MongoDb': {
                'database': 'TESTDB',
                'encryption': True,
                'encryptionKey': 'FakePassWord!',
                'password': '!54353Ffesf34',
                'replicaSet': 'FAKE-DB-531',
                'Nested': {
                    'key': 5243
                }
            },
            'second': 1,
            'myList': ['first', 'second', 'third']
        }
    },
    'MyServer': {
        'host': 'my.server.com',
        'port': 8080
    }
}


class TestConfig(ConfigParser):
    def get_config(self):
        return parsed_yml


class Spring(Configuration):
    class Data:
        class MongoDb:
            database = String()
            encryption = Boolean()
            encryptionKey = String()
            password = String()
            replicaSet = String()

            class Nested:
                key = Integer()

        second = Integer()
        myList = List()


class SuperNested(Configuration):
    __section__ = 'Spring.Data.MongoDb'

    database = String()
    encryption = Boolean()
    encryptionKey = String()
    password = String()
    replicaSet = String()

    class Nested:
        key = Integer()


class MyServer(Configuration):
    host = String()
