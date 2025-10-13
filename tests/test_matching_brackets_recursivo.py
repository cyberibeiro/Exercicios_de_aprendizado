import pytest

from exercicios_de_aprendizado.matching_brackets_recursivo import BracketMatcher


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
def test_bracket_matcher(text: str, expected: bool) -> None:
    assert BracketMatcher(text).is_paired() == expected
