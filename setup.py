#Helps in building our ml application as a package;anyone can use this package in our projects
from setuptools import find_packages,setup       #automatically find all packages in ml applicatioin
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this func. returns list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:             #open the file as a file object
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if HYPHEN_E_DOT in requirements:      #prevent infinite loop coz req.txt is also opening setup.py
            requirements.remove(HYPHEN_E_DOT)

    return requirements
    
setup(
    name="mlProject",
    version="0.0.1",
    author='HeliosX',
    author_email='vatshivam498@gmail.com',
    packages=find_packages(),           #check all the folders that hv "__init__.py" src is packet itself?
    # install_requires=['pandas','numpy','seaborn']              #all the libraries req for running;automatically install
    install_requires=get_requirements('requirements.txt')

)
