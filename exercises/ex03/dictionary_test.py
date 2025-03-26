"""Practice Writing Unit Tests for Dictionary Module"""

__author__: str = "730649282"

from dictionary import invert, count, favorite_color, bin_len


def test_invert_use_1() -> None:
    """Tests if the function inverts the values and keys"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_2() -> None:
    """Tests if the function inverts the value and key"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_edge() -> None:
    """Tests if the function returns an empty dictionary if given an empty dictionary"""
    assert invert({}) == {}


def test_count_use_1() -> None:
    """Tests if the function lists the item and its frequency in a list"""
    assert count(
        ["eggs", "eggs", "eggs", "bacon", "bacon", "grits", "sausage", "sausage"]
    ) == {"eggs": 3, "bacon": 2, "grits": 1, "sausage": 2}


def test_count_use_2() -> None:
    """Tests if the function lists the item and its frequency in a list"""
    assert count(["February", "March", "April"]) == {
        "February": 1,
        "March": 1,
        "April": 1,
    }


def test_count_edge() -> None:
    """Tests if the function returns an empty dictionary if given an empty list"""
    assert count([]) == {}


def test_favorite_color_edge() -> None:
    """Tests if the function returns the string of the first most popular color"""
    assert (
        favorite_color({"Ashley": "pink", "Danny": "orange", "Kesha": "yellow"})
        == "pink"
    )


def test_favorite_color_use_1() -> None:
    """Tests if the function returns the string of the most popular color"""
    assert (
        favorite_color(
            {"Keke": "purple", "Party": "black", "Becky": "black", "Resha": "blue"}
        )
        == "black"
    )


def test_favorite_color_use_2() -> None:
    """Tests if the function returns the string of the most popular value"""
    assert (
        favorite_color({"Drake": "red", "Kim": "apples", "Stacy": "apples"}) == "apples"
    )


def test_bin_len_use_1() -> None:
    """Tests if the function groups words of the same length together"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_2() -> None:
    """Tests if the function doesn't repeat values in the set"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge() -> None:
    """Tests if the function groups strings with the same character length together"""
    assert bin_len([":-)", "yo!", "\U0001f44d"]) == {
        3: {":-)", "yo!"},
        1: {"\U0001f44d"},
    }
