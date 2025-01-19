from setuptools import find_packages,setup

setup(
    name = 'MLproject',
    version = '0.0.1',
    author  = 'Ankit Bista',
    author_email = 'ankitbista1406@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas','numpy','seaborn'],
)