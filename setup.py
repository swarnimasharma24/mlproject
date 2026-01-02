from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str)->List[str]:
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if(requirements.__contains__("-e .")):
            requirements.remove("-e .")

        return requirements

setup(
    name="ml_project",
    version="0.0.1",
    author="Swarnima",
    author_email="swarnimasharma05@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
       
)