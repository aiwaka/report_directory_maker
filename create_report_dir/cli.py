import os
import sys
import re

import fire


def get_config():
    """コンフィグデータを取得する"""


def detect_invalid_char(name: str) -> bool:
    """ディレクトリ名として使えない文字またはピリオドを含む場合Trueを返す"""
    return re.search(r'[\\|/|:|?|.|"|<|>|\|]', name) is not None


def error_print(s: str):
    print(f"\x1b[38;5;9m{s}\x1b[m")


def create_dir(dir_name: str):
    """カレントディレクトリ直下にディレクトリを作成する."""
    cwd = os.getcwd()
    if detect_invalid_char(dir_name):
        error_print(f"The directory name '{dir_name}' is not available.")
        sys.exit(1)
    new_full_path = os.path.normpath(cwd + "/" + dir_name)

    try:
        os.mkdir(new_full_path)
    except FileExistsError as e:
        error_print(str(e))
        sys.exit(2)
    else:
        print(f"created the directory \x1b[38;5;11m'{new_full_path}'\x1b[m")


def app(dir_name):
    """アプリ本体"""
    dir_name = str(dir_name)
    create_dir(dir_name)


def main():
    fire.Fire(app)
