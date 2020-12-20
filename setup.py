from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ZenoMapper',
    license='Apache license 2.0',
    description='An Object Config Mapper (OCM)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Joseph Procopio',
    author_email='josephp27@live.com',
    packages=find_packages(exclude=['test', 'tests']),
    options={'bdist_wheel': {'universal': True}},
    url='https://github.com/josephp27/Zeno',
    install_requires=[
        'six>=1.15.0'
    ],
    keywords=['zeno', 'map-zeno', 'ocm', 'config-mapper', 'dictionaries', 'types', 'settings', 'settings-management',
              'yml', 'yaml', 'ini', 'configuration', 'parser', 'orm', 'object-mapper'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
