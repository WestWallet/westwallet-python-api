from setuptools import setup, find_packages

setup(
    name='westwallet_api',
    version='1.1.5',
    install_requires=[
        "dataclasses==0.6",
        "requests==2.22.0"
    ],
    packages=find_packages(),
    url='https://westwallet.info',
    license='Apache License 2.0',
    author='WestWallet',
    author_email='admin@westwallet.info',
    description='WestWallet Public API Python wrapper'
)
