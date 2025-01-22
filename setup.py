from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    Returns the list of reqs
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [items.replace("\n", "") for items in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name='mlopsproject',
    version='0.0.1',
    author='Ria',
    author_email='riaprasad46@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
      
      
    )