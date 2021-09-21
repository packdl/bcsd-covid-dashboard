import csv
from datetime import datetime

from playwright.sync_api import Playwright, sync_playwright

from schools import get_schools, parseschooldata, gettableheader

elem = {"Mt Holly Elementary":"MHE","Mount Holly Elementary": "MHE", "Berkeley County School District": "BCSD"}

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.bcsdschools.net/Domain/8307
    page.goto("https://www.bcsdschools.net/Domain/8307")
    
    our_element = page.query_selector("#pmi-43630")
    school_data = our_element.inner_html()

    # Get list of schools from the drop down in the page
    schools = get_schools(school_data)

    rows = []
    for school in schools:
        print(school)
        page.select_option("select[name=\"Value1_1\"]", school) #fmt: skip

        page.click('input:has-text("Search")')
        page.wait_for_timeout(1000)

        # Save header if school is Berkeley County School District
        element_handle = page.query_selector("#pmi-43630")

        # Get html of target element and parse out and store data
        div = element_handle.inner_html()
        if 'Berkeley County School District'.lower() in school.lower():
            header = gettableheader(element_handle.inner_html())
            with open("output/header.csv","a", newline="") as headerfile:
                csv.writer(headerfile).writerow((datetime.now().date(),) + header)
        rows.append(parseschooldata(div))

    with open("output/data.csv", "a", newline="") as fp:
        cvswriter = csv.writer(fp)
        cvswriter.writerows(rows)

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
