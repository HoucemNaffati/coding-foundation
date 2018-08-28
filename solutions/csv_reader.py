import csv

def header(title):
    print('\n===[ {} ]===\n'.format(title))


with open('file.csv') as csv_file:
    header('Printing CSV')

    csv_reader = csv.reader(csv_file)

    count = 0
    sum_ages = 0
    for row in csv_reader:
        count += 1
        if count == 1:
            continue

        print('Hello {}'.format(row[0]))
        sum_ages += int(row[1])

    header('Sum of ages')
    print('{}'.format(sum_ages))
