"""Practicing Dictionary Functions!"""

__author__: str = "730649282"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    empty: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in empty:
            raise KeyError("This is a Key Error!")
        empty[dictionary[key]] = key
    return empty


def count(frequencies: list[str]) -> dict[str, int]:
    values: dict[str, int] = {}
    for idx in frequencies:
        if idx in values:
            values[idx] += 1
        else:
            values[idx] = 1
    return values


def favorite_color(colors: dict[str, str]) -> str:
    fav: list[str] = []
    frequency: dict[str, int] = {}
    max: int = 0
    fav_color: str = ""
    for name in colors:
        fav.append(colors[name])
    frequency = count(fav)
    for idx in frequency:
        if frequency[idx] > max:
            max = frequency[idx]
            fav_color = idx
    return fav_color


def bin_len(list: list[str]) -> dict[int, set[str]]:
    bin: dict[int, set[str]] = {}
    for word in list:
        if len(word) in bin:
            bin[len(word)].add(word)
        else:
            bin[len(word)] = {word}
    return bin
