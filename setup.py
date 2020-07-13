import os
from setuptools import setup

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()


setup(
    name='flaskchat',
    version='0.1.3',
    packages=[''],
    url='https://github.com/da070116/flaskchat',
    license='GPL v. 3',
    author='Dubrovin Alexander',
    author_email='da070116@gmail.com',
    description='Chat ',
    install_requires=install_requires
)
