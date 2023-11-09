from setuptools import setup, find_packages

setup(
    name='westwallet_api',
    version='1.1.9',
    install_requires=[
        "dataclasses==0.6",
        "requests==2.22.0"
    ],
    packages=find_packages(),
    url='https://westwallet.io',
    license='Apache License 2.0',
    author='WestWallet',
    author_email='admin@westwallet.io',
    description='Official WestWallet Public API Python wrapper'
)
