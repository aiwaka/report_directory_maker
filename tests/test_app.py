import pytest

from create_report_dir.cli import detect_invalid_char


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("1", False),
        ("ok", False),
        (r"\\test", True),
        (r".test", True),
        (r"test.test", True),
        (r"tes?t", True),
        (r"tes/t", True),
        (r"tes\t", True),
        (r"tes:t", True),
        (r'tes"t', True),
        (r"tes<t", True),
        (r"te>st", True),
        (r"te|st", True),
    ],
)
def test_is_prime(path, expected):
    assert detect_invalid_char(path) == expected
