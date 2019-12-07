from __future__ import absolute_import
from setuptools import find_packages, setup
from os.path import dirname, join, realpath

HERE = dirname(realpath(__file__))

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

try:
    with open(join(HERE, 'reeeeeeeeee', 'VERSION'), 'r') as r:
        version = r.read()
except FileNotFoundError:
    version = '0.0.0'

with open(join(HERE, 'README.rst'), 'r') as r:
    long_description = r.read()

setup(
    name="reeeeeeeeee",
    author="Levi Noecker",
    author_email="levi.noecker@gmail.com",
    url="https://github.com/leviable/reeeeeeeeee",
    description="Raging on the command line",
    long_description=long_description,
    license="MIT",
    packages=find_packages(),
    version=version,
    install_requires=[],
    keywords="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    entry_points={
        'console_scripts': [
            're=reeeeeeeeee.__init__:reeeeeeeeee',
            'ree=reeeeeeeeee.__init__:reeeeeeeeee',
            'reee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
            'reeeeeeeeeeeeeeeeeeeeeeee=reeeeeeeeee.__init__:reeeeeeeeee',
        ]
    }
)
