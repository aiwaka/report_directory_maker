import os
import sys
import re

import fire


def get_config():
    """コンフィグデータを取得する"""


def detect_invalid_char(name: str) -> bool:
    """ディレクトリ名として使えない文字またはピリオドを含む場合Trueを返す"""
    return re.search(r'[\\|/|:|?|.|"|<|>|\|]', name) is not None


def create_dir(dir_name: str):
    """カレントディレクトリ直下にディレクトリを作成する."""
    cwd = os.getcwd()
    if detect_invalid_char(dir_name):
        print(f"\x1b[38;5;9mThe directory name '{dir_name}' is not available.\x1b[m")
        sys.exit(1)
    new_full_path = os.path.normpath(cwd + "/" + dir_name)

    print(new_full_path)


def app(dir_name):
    """アプリ本体"""
    dir_name = str(dir_name)
    create_dir(dir_name)


def main():
    fire.Fire(app)
