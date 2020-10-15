import os

from ZenoMapper.Types import *

__version__ = '0' + os.environ.get('TRAVIS_BUILD_NUMBER', '0.0')
