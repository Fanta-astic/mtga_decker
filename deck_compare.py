
import csv

# Read in the collection output
with open("testout") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1
        else: print(f'{row[0]} {row[1]} {row[2]}')
# print(myCards.read())


# deck = open("test_mono_blue.txt")
# for row in deck:
    # print(row.split(' ', 1)) # split the first element from the following ones


# this takes in a deck with goldfish format and returns a csv
# Will be in a format that we can compare to our collection
with open('test_mono_blue.txt', 'r') as deck:
    stripped = (line.strip() for line in deck)
    lines = (line.split(' ', 1) for line in stripped if line)
    with open('deck.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('count', 'name'))
        writer.writerows(lines)
