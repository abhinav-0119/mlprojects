# BUILDING YOUR APPLICATION AS PACKAGE 
from setuptools import find_packages, setup
from typing import List

something = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if something in requirements:
            requirements.remove(something)

    return requirements

setup(
    name="mlprojects",
    version="0.0.1",
    author="ABHINAV ANAND",
    author_email="anandabhinav0119@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)