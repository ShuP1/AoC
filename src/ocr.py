"""Convert Advent of Code ASCII art"""
"""From https://github.com/bsoyka/advent-of-code-ocr"""

ALPHABET_6 = {
    ".##.\n#..#\n#..#\n####\n#..#\n#..#": "A",
    "###.\n#..#\n###.\n#..#\n#..#\n###.": "B",
    ".##.\n#..#\n#...\n#...\n#..#\n.##.": "C",
    "####\n#...\n###.\n#...\n#...\n####": "E",
    "####\n#...\n###.\n#...\n#...\n#...": "F",
    ".##.\n#..#\n#...\n#.##\n#..#\n.###": "G",
    "#..#\n#..#\n####\n#..#\n#..#\n#..#": "H",
    ".###\n..#.\n..#.\n..#.\n..#.\n.###": "I",
    "..##\n...#\n...#\n...#\n#..#\n.##.": "J",
    "#..#\n#.#.\n##..\n#.#.\n#.#.\n#..#": "K",
    "#...\n#...\n#...\n#...\n#...\n####": "L",
    ".##.\n#..#\n#..#\n#..#\n#..#\n.##.": "O",
    "###.\n#..#\n#..#\n###.\n#...\n#...": "P",
    "###.\n#..#\n#..#\n###.\n#.#.\n#..#": "R",
    ".###\n#...\n#...\n.##.\n...#\n###.": "S",
    "#..#\n#..#\n#..#\n#..#\n#..#\n.##.": "U",
    "#...\n#...\n.#.#\n..#.\n..#.\n..#.": "Y",
    "####\n...#\n..#.\n.#..\n#...\n####": "Z",
}


def ocr_str(input_text, *, fill_pixel = "#", empty_pixel = "."):
    input_text = input_text.replace(fill_pixel, "#").replace(empty_pixel, ".")
    return _convert_6([list(line) for line in input_text.split("\n")])


def ocr_array(array, *, fill_pixel = "#", empty_pixel = "."):
    return _convert_6([[
        "#" if pixel == fill_pixel else "." if pixel == empty_pixel else ""
        for pixel in line
    ] for line in array])


def _convert_6(array):
    rows, cols = len(array), len(array[0])
    if any(len(row) != cols for row in array):
        raise ValueError("all rows should have the same number of columns")
    if rows != 6:
        raise ValueError("incorrect number of rows (expected 6)")
    return "".join(ALPHABET_6["\n".join("".join(row[index]) for row in array)]
        for index in (slice(start, start + 4) for start in range(0, cols, 5)))
