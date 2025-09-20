import pytest

from exercicios_de_aprendizado.matching_brackest import BracketMatcher


@pytest.mark.parametrize(
    "text,expected",
    [
        ("{what is (42)}?", True),
        ("[text}", False),
        ("()[]{}", True),
        ("([{}])", True),
        ("([)]", False),
        ("", True),
        ("hello world", True),
        ("(", False),
        ("]", False),
        ("(([])", False),
    ],
)
def test_bracket_matcher(text, expected) -> None:
    assert BracketMatcher(text).is_paired() == expected
    assert BracketMatcher(text).is_paired() == expected
