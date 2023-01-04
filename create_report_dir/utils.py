import re


def error_print(s: str):
    print(f"\x1b[38;5;9m{s}\x1b[m")


def detect_invalid_char(name: str) -> bool:
    """ディレクトリ名として使えない文字またはピリオドを含む場合Trueを返す"""
    return re.search(r'[\\|/|:|?|.|"|<|>|\|]', name) is not None
