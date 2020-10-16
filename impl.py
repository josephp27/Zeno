from ZenoMapper.Configuration import ConfigParser, Configuration
from ZenoMapper.Types import String


class MyConfig(ConfigParser):

    def get_config(self):
        return {'general': 'fdgfds'}


class GG(Configuration):
    general = String()
