import csv, os

# stores file names in a list
path = input('\n'"Enter absolute path to directory: ").strip()
filenames = os.listdir(path)
filenames.remove(".DS_Store")
filenames.sort()
id_count = 0

# creates csv and adds desired headers
with open('manifest.csv', 'w', newline = '', encoding='utf-8') as csvfile:
    fieldnames = ['id','filename']
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames = fieldnames)
    writer.writeheader()

# writes file names and numbers to columns in csv.
    for filename in filenames:
        id_count += 1
        writer.writerow({'id':id_count, 'filename':filename})

print('\n'"Complete!")
