import os

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ZenoMapper',
    packages=['ZenoMapper'],
    license='Apache license 2.0',
    description='An Object Config Mapper (OCM)',
    version='0.37.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Joseph Procopio',
    author_email='josephp27@live.com',
    url='https://github.com/josephp27/Zeno',
    keywords=['Zeno', 'OCM', 'Config', 'Configuration', 'Mapper', 'Object'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
