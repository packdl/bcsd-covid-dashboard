import csv
from datetime import datetime

from playwright.sync_api import Playwright, sync_playwright

from schools import get_schools, parseschooldata, gettableheader

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to COIVD Dashboard at https://www.bcsdschools.net/Domain/8307
    page.goto("https://www.bcsdschools.net/Domain/8307")
    
    # Get list of schools from the drop down in the page
    our_element = page.query_selector("#pmi-43630")
    school_data = our_element.inner_html()
    schools = get_schools(school_data)

    # Get COVID data for each school
    rows = []
    for school in schools:
        print(school)
        page.select_option("select[name=\"Value1_1\"]", school) #fmt: skip

        page.click('input:has-text("Search")')
        page.wait_for_timeout(1000)
        
        element_handle = page.query_selector("#pmi-43630")
        
        # Save header if school is Berkeley County School District
        if 'Berkeley County School District'.lower() in school.lower():
            retrieve_header(element_handle)

        # Get COVID data for school and store in list
        div = element_handle.inner_html()
        rows.append(parseschooldata(div))

    # Write data for schools to text file
    with open("output/data.csv", "a", newline="") as fp:
        cvswriter = csv.writer(fp)
        cvswriter.writerows(rows)

    # ---------------------
    context.close()
    browser.close()

def retrieve_header(element_handle):
    header = gettableheader(element_handle.inner_html())
    with open("output/header.csv","a", newline="") as headerfile:
        csv.writer(headerfile).writerow((datetime.now().date(),) + header)

with sync_playwright() as playwright:
    run(playwright)
