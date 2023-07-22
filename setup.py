from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='ML Projects',
version='0.0.1',
author='Chirag',
author_email='chirag1346@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)



"""
The provided Python code is a script that sets up a package called "ML Projects" using setuptools.

It defines a function get_requirements(file_path:str) that reads the requirements from a file, removes the '-e .' entry if present, and returns the list of requirements.

Here's a breakdown of the code:

1. The script imports the necessary functions from setuptools and typing.

2. It defines a constant variable HYPEN_E_DOT with the value '-e .', which is used to identify and remove the local package reference in the requirements.

3. The function get_requirements(file_path:str) takes a file path as input and returns a list of requirements read from that file. It reads the file line by line, removes the newline characters, and adds each requirement to the requirements list. 
   If the '-e .' entry is found in the requirements list, it is removed.

4. The setup() function is called to set up the package. It takes various arguments like package name, version, author, author email, and the list of packages to include.
   The find_packages() function is used to automatically discover and include all packages in the project.

5. The install_requires argument of the setup() function is set to the result of get_requirements('requirements.txt'), which includes the list of required dependencies for the project, read from the 'requirements.txt' file.

 Overall, this script is a simple setup file for a Python package named "ML Projects," which includes the necessary packages specified in the 'requirements.txt' file for the project. 
"""