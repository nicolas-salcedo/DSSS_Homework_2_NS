from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Nicolás Salcedo",
    author_email="nicolas.salcedo@fau.de",
    packages=find_packages(),
    install_requires=["random"]
)