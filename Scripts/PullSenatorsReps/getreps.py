""" This script is gives a list of the senators and representatives based on the
listings on the house and senate.gov websites.

The output of this program will later be a csv file, but at the moment it
just prints to stdout.
To save the info to a file run it like so:
python getreps.py > <FILENAME>
"""

# import selenium
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
print('Senators')
for row in sen_rows:
    senator = row.find_elements_by_tag_name('td')
    if len(senator) < 1:
        continue
    if senator[1].text == 'California':
        print(senator[0].text)
        print(senator[0].find_element_by_tag_name('a').get_attribute('href'))
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
for rep in cali_reps:
    rep_data = rep.find_elements_by_tag_name('td')
    if len(rep_data) < 1:
        continue
    print(rep_data[1].text.replace('(link is external)', ''))
    print(rep_data[1].find_element_by_tag_name('a').get_attribute('href'))


# Closes the driver
driver.close()