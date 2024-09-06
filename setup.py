from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='index_docs',
    version='1.0',
    description='Indexing documentation files from instill.tech repository',
    long_description='Indexing documentation files from instill.tech repository',
    author='George Strong',
    author_email='george.strong@instill.tech',
    license='AGPL-3.0',
    python_requires=">=3.12.2",
    packages=find_packages(),
    install_requires=required)
