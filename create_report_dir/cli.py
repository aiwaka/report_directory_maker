import os
import sys
from typing import Union

import fire

from .utils import detect_invalid_char, error_print
from .temp import latex_template


def get_config():
    """コンフィグデータを取得する"""


def create_dir(dir_name: str, force: bool) -> str:
    """カレントディレクトリ直下にディレクトリを作成する. 作成した結果のフルパスを返す"""
    cwd = os.getcwd()
    if detect_invalid_char(dir_name):
        error_print(f"The directory name '{dir_name}' is not available.")
        sys.exit(1)
    new_full_path = os.path.normpath(cwd + "/" + dir_name)

    try:
        os.mkdir(new_full_path)
    except FileExistsError as e:
        # TODO: forceオプションを有効にする
        error_print(str(e))
        sys.exit(2)
    else:
        print(f"created the directory \x1b[38;5;11m'{new_full_path}'\x1b[m")

    return new_full_path


def create_file(path: str, title: str, author: str):
    with open(path, mode="w") as f:
        f.write(latex_template.format(title=title, author=author))
    print(f"created the file \x1b[38;5;11m'{path}'\x1b[m")


def app(
    dir_name, filename: Union[str, None] = None, force: bool = False, title: str = ""
):
    """アプリ本体"""
    dir_name = str(dir_name)
    if filename is None:
        filename = dir_name + ".tex"
    elif detect_invalid_char(filename):
        error_print(f"The file name '{filename}' is not available.")
        sys.exit(1)
    else:
        filename += ".tex"

    new_full_path = create_dir(dir_name, force)
    filepath = new_full_path + "/" + filename
    create_file(filepath, title, "author")


def main():
    fire.Fire(app)
