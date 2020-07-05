""" This script is gives a list of the senators and representatives based on the
listings on the house and senate.gov websites.

The output of this program will later be a csv file, but at the moment it
just prints to stdout.
To save the info to a file run it like so:
python getreps.py > <FILENAME>
"""

# imports
import csv
from selenium import webdriver

# Driver Setup
driver = webdriver.Firefox()

# mark links for senate and reps.gov sites
senate = 'https://www.senate.gov/senators/index.htm'
reps   = 'https://www.house.gov/representatives'

# Start with senate
driver.get(senate)
# Gets the senator table and rows
sen_table = driver.find_element_by_id('listOfSenators')
sen_rows = sen_table.find_elements_by_tag_name('tr')

# Goes through each row and checks that the length isn't 0
# and that the state is California
# Prints the name of the representative and their link
with open('senators.csv', 'w', newline='') as csvfile:
    sen_writer = csv.writer(csvfile, delimiter = ',')
    sen_writer.writerow(['Senator', 'State', 'Website'])
    print('Senators')
    for row in sen_rows:
        senator = row.find_elements_by_tag_name('td')
        if len(senator) < 1:
            continue
        if senator[1].text == 'California':
            name = senator[0].text
            website = senator[0].find_element_by_tag_name('a').get_attribute('href')
            sen_writer.writerow([name, 'California', website])
            print(name,website)
    print()
# Representatives
driver.get(reps)

# Gets all the representatives tables
rep_tables = driver.find_elements_by_tag_name('table')
cali_table = rep_tables[0]


print("Representatives")
# Looks for the california table
for table in rep_tables:
    caption = table.find_element_by_tag_name('caption')
    if caption.text == 'California':
        cali_table = table
        break
# Gets each row of the california representatives table and prints the name and link
cali_reps = cali_table.find_elements_by_tag_name('tr')

with open('representatives.csv', 'w', newline='') as csvfile:
    rep_writer = csv.writer(csvfile, delimiter = ',')
    rep_writer.writerow(['Representative', 'State', 'Website', 'Committee'])
    for rep in cali_reps:
        rep_data = rep.find_elements_by_tag_name('td')
        if len(rep_data) < 1:
            continue
        name = rep_data[1].text.replace('(link is external)', '')
        website = rep_data[1].find_element_by_tag_name('a').get_attribute('href')
        committee = rep_data[5].text
        rep_writer.writerow([name, 'California', website, committee])
        print(name,website,committee)


# Closes the driver
driver.close()