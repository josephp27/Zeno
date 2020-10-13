import os

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = ''
with open('__version__', 'rw+') as fh:
    set_version = fh.readline()
    build_number = os.getenv('TRAVIS_BUILD_NUMBER', '0.0')

    if not set_version:
        VERSION = '0.' + build_number
        fh.write(VERSION)
    else:
        VERSION = set_version


setup(
    name='ZenoMapper',
    license='Apache license 2.0',
    description='An Object Config Mapper (OCM)',
    version=VERSION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Joseph Procopio',
    author_email='josephp27@live.com',
    packages=find_packages(exclude=['test', 'tests']),
    options={'bdist_wheel' : {'universal': True}},
    url='https://github.com/josephp27/Zeno',
    keywords=['Zeno', 'OCM', 'Config', 'Configuration', 'Mapper', 'Object'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
