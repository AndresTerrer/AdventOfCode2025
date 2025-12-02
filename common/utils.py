"""
Common logic to load data from txt
"""

import numpy as np
import re


class Day:
    def __init__(self, path: str):
        self.path = path
        pass


def read_lines(text_file_path: str) -> list[str]:
    """
    read txt and return a list of lines
    """
    with open(text_file_path) as f:
        line_list = f.readlines()

    # Remove \n characters
    line_list = [
          line.replace("\n", "") for line in line_list
    ]

    return line_list


def read_columns(text_file_path: str) -> list[str]:
    """
    read txt and return a list of each string column.
    assumes a rectangular input
    """

    with open(text_file_path) as f:
        lines = f.readlines()

    columns = []
    for i in range(len(lines)):
        columns.append(
            "".join([line[i] for line in lines])
        )

    return columns


def read_as_character_array(text_file_path: str) -> np.array:
    """
    Read txt as an array of idividual characters
    """

    with open(text_file_path) as f:
        lines = f.readlines()
        lines = [
            line.replace("\n", "") for line in lines
        ]
        characters = [
            [char for char in line] for line in lines
        ]

    return np.array(characters)


def as_integer_array(line_list: list[str]) -> np.array:
    """
    Try to interpret the loaded data as an array of iteger values

    """
    lines_as_integers = [re.findall(r"\d+", line) for line in line_list]

    return np.array(lines_as_integers).astype(int)


def read_diagonals(arr: np.array, inverse=False) -> list:
    """
    Read all diagonals

    characters in the same diagonals satisfy:
    i - j = Constant.
    (i + j  = constant for inverse diagonals)
    where i and j are the indeces of the matrix.

    inverse bool: select inverse diagonal, default False.

    Compute this value for all elemenents of the matrix, then
    select in groups and return a list, one element for each constant
    """

    i_index, j_index = np.indices(arr.shape)

    if inverse:
        groups_arr = i_index + j_index

    else:
        groups_arr = i_index - j_index

    max, min = groups_arr.max(), groups_arr.min()

    diagonals = []

    for i in range(min, max + 1, 1):
        diagonals.append(
            arr[groups_arr == i]
        )

    return ["".join([element for element in diag]) for diag in diagonals]


def integer_lists(line_list: list[str]) -> list[list[int]]:
    """
    Try to interpret txt lines as lists of integers
    """
    data = [re.findall(r"\d+", line) for line in line_list]
    return [[int(x) for x in record] for record in data]