#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# metadata
"A level file editor for Minecraft: Pi Edition"
__version__ = "1.0"
__license__ = "AGPLv3+"
__author__ = "mcpiscript"
__email__ = "mcpiscript@gmail.com"
__url__ = "https://github.com/mcpiscript"
__prj__ = "editpi"

from setuptools import setup
import glob

def get_translation_files():
    return_value =  list()
    for file in list(glob.iglob("src/assets/translations/**",  recursive=True)):
        return_value.append(file[4:])
    return return_value


with open("README.md") as file:
    long_description = file.read()

setup(
    name="editpi",
    version="1.0",
    description="A level file editor for Minecraft: Pi Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="mcpiscript",
    author_email="mcpiscript@gmail.com",
    maintainer="Alexey Pavlov",
    maintainer_email="pezleha@duck.com",
    url="https://github.com/mcpiscript",
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)"
    ],
    packages=["editpi"],
    install_requires=["pynbt"],
    package_dir={"editpi": "src"},
    include_package_data=True,
    package_data={"editpi": ["assets/img/*.png"]+ get_translation_files()},
    extras_require={"pyqt5": ["pyqt5"]},
    entry_points={
        "console_scripts": ["editpi = editpi:main", "mcpiedit = editpi:main"]
    },
)
