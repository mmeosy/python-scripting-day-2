import csv
def writecsvfile(data):
    with open('data.csv', 'a') as file:
        myFile = csv.writer(file)
        myFile.writerow(data)
