# BUILDING YOUR APPLICATION AS PACKAGE 
'''setup.py is used to package a Python project and 
make it installable. It allows Python to recognize 
the project as a package so that its modules can 
be imported cleanly and managed using package management 
tools like pip
'''
'''setup.py is not responsible for making folders into packages;
 __init__.py does that. setup.py is responsible for packaging 
 and installing the entire project so that Python and pip can 
 manage it properly.
'''
from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements

setup(
    name="mlprojects",
    version="0.0.1",
    author="ABHINAV ANAND",
    author_email="anandabhinav0119@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
'''def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    return requirements'''