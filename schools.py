from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

schools = [
    "Berkeley County School District",
    "Mount Holly Elementary",
]


def parseschooldata(div: str) -> tuple:
    """Parse school data from div string"""
    output = []

    soup = BeautifulSoup(div.strip(), "html.parser")
    rows = soup.find_all("td")

    for row in rows:
        # print(row.contents)
        if len(row.contents) == 1 and isinstance(row.contents[0], NavigableString):
            output.append(row.contents[0].string.strip())
        elif (
            len(row.contents) == 1
            and isinstance(row.contents[0], Tag)
            and row.contents[0].name == "time"
        ):
            output.append(row.contents[0].attrs["datetime"])
        else:
            continue
    output = tuple(output)

    return output


def get_schools(school_data):
    """Get school names from div string and return as a list."""
    schools = []
    soup = BeautifulSoup(school_data.strip(), "html.parser")
    school_select = soup.find("select", attrs={"id": "Value1_1"})

    for option in school_select.children:
        if option.name == "option":
            school = option.attrs["value"]
            schools.append(school)
    return schools


if __name__ == "__main__":
    with open("output/div.html", "r") as fp:
        data = fp.read()
        print(get_schools(data))
        # print(parseschooldata(data))
