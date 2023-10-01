import csv

temple_dicts = []

with open("ChurchofJesusChristTemples.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        temple_dicts.append(row)

count = 0

for line in temple_dicts:
    print(f"displayPoint(graphicsLayer, '{line['Temple']}', {line['Latitude']}, {line['Longitude']}, '{line['Status']}', '{line['Dedication Date']}');")
    count = count + 1

area_dicts = []

print(f"Imported {count} temples.")  # This line of code is just to make sure that each temple was imported from the CSV file.