"""
Copyright (C) 2022  Alexey Pavlov

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    USA
"""

import pynbt
import subprocess


def remove_header(filename: str):
    # with open(filename,  "rb") as file:
    #   data = file.read()
    # with open(filename,  "wb") as write_file:
    #    write_file.write(data[8:])
    # This is WIP code! Do not use!

    return subprocess.Popen(
        ["pi-nbt", "remove-header", filename, filename + "_temp.dat"]
    ).wait()


def add_header(filename: str):
    return subprocess.Popen(
        ["pi-nbt", "add-header", filename + "_temp.dat", filename]
    ).wait()


def load_nbt(filename: str, header=False):
    if header:
        remove_header(filename)

    with open(filename + "_temp.dat", "rb") as nbt:
        nbt = pynbt.NBTFile(io=nbt, little_endian=True)
        return nbt


def save_nbt(nbt: pynbt.NBTFile, filename: str, header=True):

    with open(filename + "_temp.dat", "wb") as writefile:
        nbt.save(io=writefile, little_endian=True)

    if header:
        add_header(filename)


__all__ = ["pynbt", "remove_header", "add_header", "load_nbt", "save_nbt"]
