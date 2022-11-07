from setuptools import find_packages
from setuptools import setup

setup(
    name="sensor",
    version="0.0.1",
    author='MR.BHAGWAT CHATE',
    author_email="bhagwat.chate25@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo==4.2.0"]
)