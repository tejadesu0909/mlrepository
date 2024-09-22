from setuptools import find_packages, setup
from typing import List

HYPHEH_E_DOT = '-e .'
 
def get_requirement(file_path:str)-> List[str]:
    '''
        This function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] 

        if HYPHEH_E_DOT in requirements:
            requirements.remove(HYPHEH_E_DOT)

        return requirements

setup(
    name = 'mlrepository',
    version = '0.0.1', 
    author = 'Teja',
    author_email= 'desu.teja5@gmail.com',
    packages=find_packages(),
    # install_requires = ['numpy', 'pandas', 'seaborn']
    install_requires = get_requirement('requirements.txt')

# C:\Users\desut\Desktop\mlrepository\
)