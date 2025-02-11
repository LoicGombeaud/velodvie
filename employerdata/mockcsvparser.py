import csv
from employerdata.employer import Employer

class MockCSVParser:
    def __init__(self, file_paths, delimiter=';'):
        self.file_paths, self.delimiter = file_paths, delimiter
        self.delimiter = delimiter
        self.employers = []

    def parse(self):
        for file_path in self.file_paths:
            with open(file_path) as csv_file:
                employer_reader = csv.reader(csv_file, delimiter=self.delimiter)
                for line in employer_reader:
                    csv_employer_name = line[0]
                    try:
                        employer = next(filter(lambda employer: employer.name == csv_employer_name, self.employers))
                    except StopIteration:
                        csv_employer_street_address = line [1]
                        employer = Employer(csv_employer_name, csv_employer_street_address)
                        self.employers.append(employer)
                    employer.add_employee(line[2])
        return self.employers
