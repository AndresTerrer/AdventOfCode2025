"""
Create a new folder with empty notebook, data.txt and test.txt files.
"""

import os
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Create new day folder")
    parser.add_argument(
        "--day",
        type=int,
        default=-1,
        help="Make a folder for this day number",
    )
    params = parser.parse_args()

    # Determine base path
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))  # For .py files
    except NameError:
        base_path = os.getcwd()  # For interactive environments

    # Folder name
    folder = os.path.join(base_path, f"Day_{params.day:02}")

    # Create the folder and files
    os.makedirs(folder, exist_ok=True)
    open(os.path.join(folder, "test.txt"), "w").close()
    open(os.path.join(folder, "data.txt"), "w").close()
    open(os.path.join(folder, "Notebook.ipynb"), "w").close()

    print(f"Folder created: {folder}")


if __name__ == "__main__":
    main()
