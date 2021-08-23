from bs4 import BeautifulSoup

schools = [
    "Berkeley County School District",
    "Adult Education / Head Start",
    "Central Offices",
    "Transportation",
    "Maintenance",
    "Technology",
    "Berkeley Alternative",
    "Berkeley Elementary",
    "Berkeley High School",
    "Berkeley Intermediate",
    "Berkeley Middle",
    "Berkeley Middle College",
    "Boulder Bluff Elementary",
    "Bowens Corner Elementary",
    "Cainhoy Elementary",
    "Cane Bay Elementary",
    "Cane Bay High",
    "College Park Elementary",
    "College Park Middle",
    "Cross Elementary",
    "Cross High",
    "Daniel Island School",
    "Devon Forest Elementary",
    "Foxbank Elementary",
    "Goose Creek Elementary",
    "Goose Creek High",
    "Hanahan Elementary",
    "Hanahan High",
    "Hanahan Middle",
    "H.E. Bonner Elementary",
    "Howe Hall Aims",
    "J.K. Gourdin Elementary",
    "Macedonia Middle",
    "Marrington Elementary",
    "Marrington Middle",
    "Mount Holly Elementary",
    "Nexton Elementary",
    "Philip Simmons Elementary",
    "Philip Simmons High",
    "Philip Simmons Middle",
    "Sangaree Elementary",
    "Sangaree Intermediate",
    "Sangaree Middle",
    "Sedgefield Middle",
    "St. Stephen Elementary",
    "St. Stephen Middle",
    "Stratford High",
    "Timberland High",
    "Westview Elementary",
    "Westview Middle",
    "Westview Primary",
    "Whitesville Elementary",
]


def parseschooldata(div: str) -> tuple:
    with open("./output/div.html", "r") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        rows = soup.find_all("td")
        for row in rows:
            print(row.contents)

    return (1,)


if __name__ == "__main__":
    parseschooldata("hello")
