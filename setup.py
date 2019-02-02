from setuptools import setup, find_packages
# To use a consistent encoding
# from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# with open('README.rst') as f:
#     long_description = f.read()

setup(
    name='algopy',
    version='1.0.0',
    description='A Python algorithms module for learning',
    long_description=open('README.rst').read(),
    # Author details
    author='Soham Dutta',
    author_email='soham.dutta.analyst@gmail.com',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages()
)
