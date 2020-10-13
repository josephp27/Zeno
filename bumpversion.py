import os

with open('ZenoMapper/__version__', 'w+') as fh:
    build_number = os.getenv('TRAVIS_BUILD_NUMBER', '0.0')
    fh.write('0.' + build_number)
