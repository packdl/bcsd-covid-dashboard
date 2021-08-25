import csv
from datetime import datetime

from playwright.sync_api import Playwright, sync_playwright
from bs4 import BeautifulSoup

from schools import get_schools, parseschooldata

elem = {"Mount Holly Elementary": "MHE", "Berkeley County School District": "BCSD"}

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.bcsdschools.net/Domain/8307
    page.goto("https://www.bcsdschools.net/Domain/8307")
    
    our_element = page.query_selector("#pmi-43630")
    school_data = our_element.inner_html()

    schools = get_schools(school_data)

    rows = []
    for school in schools:
        print(school)
        page.select_option("select[name=\"Value1_1\"]", school) #fmt: skip

        page.click('input:has-text("Search")')
        page.wait_for_timeout(1000)

        # Screenshot school district info
        element_handle = page.query_selector("#pmi-43630")
        if school in elem:
            element_handle.screenshot(
                path=f"output/screenshot{elem[school]}{datetime.today()}.png"
            )
        div = element_handle.inner_html()
        rows.append(parseschooldata(div))

    with open("output/data.csv", "a", newline="") as fp:
        cvswriter = csv.writer(fp)
        cvswriter.writerows(rows)

    # ---------------------
    context.close()
    browser.close()




with sync_playwright() as playwright:
    run(playwright)


# Select School
# page.select_option('select[name="Value1_1"]', "Mount Holly Elementary")

# Click input:has-text("Search")
# page.click('input:has-text("Search")')

# page.wait_for_timeout(1000)

# page1.click("#pmi-43630")
# print(element_handle.text_content())

# print(elmt_hdle.inner_html())

# element_handle.screenshot(path=f"output/screenshotMHE{datetime.today()}.png")
