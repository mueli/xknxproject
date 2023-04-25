"""Test utilities."""
import pytest

from xknxproject.util import parse_dpt_type


@pytest.mark.parametrize(
    ("dpt_string", "expected"),
    [
        ("DPT-1", {"main": 1, "sub": None}),
        ("DPT-1 DPST-1-1", {"main": 1, "sub": 1}),
        ("DPT-7 DPST-7-1", {"main": 7, "sub": 1}),
        ("DPST-5-1", {"main": 5, "sub": 1}),
        ("DPT-1 DPT-5", {"main": 5, "sub": None}),
        ("DPT-14 DPST-14-1", {"main": 14, "sub": 1}),
        ("DPST-6-10", {"main": 6, "sub": 10}),
        ("Wrong", None),
        ("DPT-Wrong", None),
        ("DPST-1-Wrong", None),
        ("DPST-5", None),
        ([], None),
        (None, None),
    ],
)
def test_parse_dpt_type(dpt_string, expected):
    """Test parsing of DPT from ETS project."""
    assert parse_dpt_type(dpt_string) == expected
