import csv

with open("test.csv", "w", newline="") as file:
    writer = csv.writer(file)
    value = ['Name', 'Cell', 'Profession', 'Email']
    writer.writerow(value)
    writer.writerow(['Jaico', '2405659609', 'DevOps Engineer','jaiconak@gmail'])
