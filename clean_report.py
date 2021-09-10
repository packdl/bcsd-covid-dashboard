import sys

from bs4 import BeautifulSoup as soup


def clean(input="./output/report.md", output="./output/report.md"):

    with open(input, "r") as infile:
        data = infile.read()
        markup = soup(data, "html.parser")
        styles = markup.find_all("style")
        for style in styles:
            style.decompose()

        with open(output, "w") as outfile:
            outfile.write(str(markup))


if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        clean()
    elif len(args) == 2:
        clean(args[1])
    elif len(args) == 3:
        clean(args[1], args[2])
    else:
        print("Usage: clean_report <input_file> <output_file>")
        sys.exit(1)

    clean()
