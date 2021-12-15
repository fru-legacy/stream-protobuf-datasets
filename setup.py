from setuptools import setup, find_packages

setup(
    name='stream-protobuf-datasets',
    version='0.0.1',
    packages=find_packages(include=['streamdatasets', 'streamdatasets.*']),
    install_requires=[
        'betterproto',
        'requests'
    ]
)