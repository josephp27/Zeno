from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Zeno',  # How you named your package folder (MyLib)
    packages=['Zeno'],  # Chose the same as "name"
    version='0.4.1',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='An Object Config Mapper (OCM)',  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Joseph Procopio',  # Type in your name
    author_email='josephp27@live.com',  # Type in your E-Mail
    url='https://github.com/josephp27/Zeno',  # Provide either the link to your github or to your website
    download_url='https://github.com/josephp27/Zeno/archive/0.4.1.tar.gz',  # I explain this later on
    keywords=['Zeno', 'OCM', 'Config', 'Configuration', 'Mapper', 'Object'],  # Keywords that define your package best
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)