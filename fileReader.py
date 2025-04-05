import csv

temple_dicts = []

with open("ChurchofJesusChristTemples.csv", 'r', encoding="utf-8") as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        temple_dicts.append(row)

count = 0

for line in temple_dicts:
    print(f"displayPoint(graphicsLayer, '{line['Temple']}', {line['Latitude']}, {line['Longitude']}, '{line['Status']}', '{line['Dedication Date']}');")
    count = count + 1

area_dicts = []

print(f"Imported {count} temples.")  # This line of code is just to make sure that each temple was imported from the CSV file.

prediction_dicts = []

with open("Predictions.csv", 'r', encoding="utf-8") as p_file:
    csv_prediction_reader = csv.DictReader(p_file)
    for row in csv_prediction_reader:
        prediction_dicts.append(row)

for line in prediction_dicts:
    print(f"displayPoint(graphicsLayer, '{line['Location']}', {line['Latitude']}, {line['Longitude']}, 'Prediction', 'Confidence Level: {line['Confidence Level']}');")