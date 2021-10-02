# Introduction
Berkeley County School District maintains an official [COVID Dashboard](https://www.bcsdschools.net/Domain/8307). The South Carolina Department of Health and Environmental Control maintains a [web page](https://scdhec.gov/covid19/covid-19-data/covid-19-cases-associated-staff-students) reporting on students & staff at schools across the state of South Carolina. This repository captures data daily from the BCSD Covid Dashboard and creates an aggregated [report](output/report.md) with graphics.

# Status
![Tests](https://github.com/packdl/bcsd-covid-dashboard/actions/workflows/python-app.yml/badge.svg)
![Web Scraper](https://github.com/packdl/bcsd-covid-dashboard/actions/workflows/scrape-bcsd-update-output.yml/badge.svg)
![Report Creation](https://github.com/packdl/bcsd-covid-dashboard/actions/workflows/create-static-report.yml/badge.svg)

# Usage
We have automated the [report](output/report.md) creation using Python and Github actions. The Report and Data sections of this page give more information about the stock report and the data that has been collected. If you have knowledge of the Python programming language, you can customize one of the notebooks in the repository to answer your own specific questions.

The easiest way to get our notebooks up and running is to use MyBinder. Click the badge to launch it. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/packdl/bcsd-covid-dashboard/HEAD)

# Our Report
A [report](output/report.md) is generated Monday through Friday at 8pm with the addition of the current day's data. 
The report identifies a number of items including:
- the schools and offices being tracked
- Top 5 Schools by Student Count for current date
- Top 5 Schools by Staff Count for current date
- Top 5 Schools by Student Count for all time
- Top 5 Schools by Staff Count for all time
- A graphic showing student/staff count for each school

# Our Data
- [Raw data](output/data.csv). This is a comma separated values (csv) file created by scraping the official BCSD Covid Dashboard on a daily basis and storing the updated information for all tracked areas in one file. It may not display correctly in Github do to changes in the format of data over time. Originally the school district only tracked **School, Area, Date, Staff Count, Student Count, Datetime**. After the first two weeks of school, they altered they website to track **School, Date, Staff Count, Student Count, Staff Close Contacts, Student Close Contacts and Datetime**. The raw data file stores the captured data no matter the changed data types from the official website. It may also have duplicate records from runs taking place more than once on the same day.
- [Cleansed data](output/cleansed_data.csv). This is a CSV file in a standard format that has been cleansed from the raw data. You will find **School, Area, Date, Staff Count, Student Count, Staff Close Contacts, Student Close Contacts, Datetime** in this dataset. **Area, Staff Close Contacts and Student Close Contacts** are optional and not filled in for all records. 

# Our License
[MIT LICENSE](LICENSE)
