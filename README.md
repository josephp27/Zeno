# Zeno | An Object Config Mapper (OCM) 

<p align="center">
<a href="https://travis-ci.com/josephp27/Zeno"><img src="https://travis-ci.com/josephp27/Zeno.svg?branch=main" alt="Build" height="18"></a>
<a href="https://badge.fury.io/py/ZenoMapper"><img src="https://badge.fury.io/py/ZenoMapper.svg" alt="PyPI version" height="18"></a>
<a href="https://pepy.tech/project/zenomapper"><img src="https://pepy.tech/badge/zenomapper" alt="Downloads" height="18"></a>
<img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License" height="18"></a>
</p>

## I heard you like ORMs, so I got you an OCM.

The idea for this comes from ORMs like SqlAlchemy and how Spring Boot uses `@ConfigurationProperties`

| Library Version| Python     |
| :------------- | :----------: |
| 1.x.x | 2.7, 3.5+   |
| 0.x (Beta) | 2.7, 3.5+   |

Zeno maps your configs to objects for you.
```yaml
Spring:
  Data:
    MongoDb:
      database: TESTDB
      encryption: true
      encryptionKey: "FakePassWord!"
      password: "!54353Ffesf34"
      replicaSet: FAKE-DB-531
    second: 1
    myList:
      - first
      - second
      - third

MyServer:
  host: my.server.com
  port: 8080
```
Looks like
```python
class Spring(Configuration): #Inheriting from Configuration lets the parser know which class to modify
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
```
And can now be accessed like:
```python
spring = Spring()
spring.Data.myList  # ['first', 'second', 'third']
spring.Data.MongoDb.encryption is True  # True
```
## Don't Like Classes?
Classes are a powerful way for autocompletion, type hints and auto conversion to those types. However, if it isn't for you, calling Zeno directly can be done. The parameter to the constructor is the path within the dictionary. If no parameter is set, it will map the whole dictionary. More examples can be found [here](https://github.com/josephp27/Zeno/blob/231bb39d884cc8f30a742c68da7c6b1121128214/examples/impl.py#L61)
```python
from ZenoMapper.zeno import Zeno

zeno = Zeno('Spring.Data.MongoDb')
zeno.database  # TESTDB
```
## Install
```bash
pip install ZenoMapper
```

## Import
```python
from ZenoMapper.Configuration import ConfigParser, Configuration
from ZenoMapper.Types import String, Boolean, Integer, List
```
### Using \_\_section\_\_ to map super nested dictionaries/ignore nesting classes
```python
class MyConfig(Configuration):
    __section__ = 'Spring.Data.Mongodb'
    
    database = String()
    encryption = Boolean()
    encryptionKey = String()
    password = String()
    replicaSet = String()
```
## Using your custom configs with Zeno
Using your own configs is easy with Zeno, simply inherit from ConfigParser and instantiate the `get_config()` function. Load in your file and Zeno will do the rest.
```python
class MyConfig(ConfigParser):
    """
    loading your own config is done via subclassing the ConfigParser class and implementing the
    get_config function.
    """
    cache = None

    @staticmethod
    def get_config():
        
        # each time an object is instantiated, this is called, so let's cache the results to increase performance
        if MyConfig.cache is None:
            with open("data.yml", 'r') as stream:
                MyConfig.cache = yaml.safe_load(stream)

        return MyConfig.cache
```            
## Types
Zeno currently has 4 types, where auto conversion will happen based on the specified type. It also brings a little static typing to Python. The plan is to add more, but currently Zeno supports: `Integer`, `String`, `Boolean`, `List`. Supported types can be found [here](https://github.com/josephp27/Zeno/blob/main/ZenoMapper/Types.py)

If you have another type you'd like but it isn't supported, etc. `None` can be used to tell Zeno to not handle conversion

## Choosing what to map
Zeno is powerful. Only specify what you'd like to map and Zeno ignores the rest
```python
class Spring(Configuration):
    class Data:
        class MongoDb:
            database = String()
```
## Hold up, that's nice but I still like using dictionary methods
Well then person reading this, Zeno is for you. All Classes are dictionary class hybrids, so you can access them like plain old dictionaries when necessary.
```python
spring.Data.myList # ['first', 'second', 'third']
spring['Data']['myList'] # ['first', 'second', 'third']
spring['Data'].myList # ['first', 'second', 'third']
spring.Data['myList'] # ['first', 'second', 'third']
spring # {'Data': {'MongoDb': {'database': 'TESTDB', 'encryption': True, 'encryptionKey': 'FakePassWord!', 'password': '!54353Ffesf34', 'replicaSet': 'FAKE-DB-531'}, 'second': 1, 'myList': ['first', 'second', 'third']}}
```

## Supports
- Any parser 
  - YAML
  - INI
  - etc, as long as it parses into a dictionary
- Automatic type conversion

## Don't Break Python Naming Conventions!
Classes can fuzzy match while not breaking Python's class naming conventions
```yaml
lower:
  case_section: true
```
```python
class Lower(Configuration):
    CaseSection = Boolean()
```
