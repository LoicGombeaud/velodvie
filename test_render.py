import os
from employerdata.mockcsvparser import MockCSVParser
from employerdata.employer import Employer

os.makedirs('./render', exist_ok=True)

parser = MockCSVParser(['./mockData/pellegrin.csv'])
employers = parser.parse()
for e in employers:
    employer_html = e.generate_html()
    with open(f'./render/{e.name}.html', 'w') as employer_html_file:
        employer_html_file.write(employer_html)

