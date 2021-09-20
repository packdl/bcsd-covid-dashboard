import os

from bs4 import BeautifulSoup
import pytest

import clean_report

CONTENT = """
# Test file
This is a test file.
<style>A style </style>
<style>A second style</style>
<style content='hi'>A third style</style>

This is a [link](https://dilbert.com)
"""


def test_clean_report(tmp_path):
    input, output = tmp_path / "testreport.md", tmp_path / "testreport-cleansed.md"
    input.write_text(CONTENT)
    clean_report.clean(input, output)

    with open(input, "r") as original, open(output, "r") as modified:
        modified_data = modified.read()

        original_data = original.read()
        non_style_strings = [
            "# Test file",
            "This is a test file.",
            "This is a [link](https://dilbert.com)",
        ]
        for s in non_style_strings:
            assert s in modified_data
            assert s in original_data

        assert "<style" in original_data

        modified_soup = BeautifulSoup(modified_data, "html.parser")
        assert modified_soup.find_all("style") == []

        original_soup = BeautifulSoup(original_data, "html.parser")
        assert len(original_soup.find_all("style")) == 3


def test_fnf_clean_report():
    with pytest.raises(FileNotFoundError):
        clean_report.clean("fnf.txt", "fnf2.txt")
