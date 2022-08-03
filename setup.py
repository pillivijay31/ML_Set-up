from setuptools import setup
from typing import List


#Declaring variables for setup functions
PROJECT_NAME="Housing-predictor"
VERSION="0.0.1"
AUTHOR="Vijay Pilli"
DESCRIPTION="This is Housing Prediction Regression Problem"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file
    
    return: This function is going to return a list which contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
 

)

if __name__=="__main__":
    print(get_requirements_list())