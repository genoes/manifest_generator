import csv, os

# stores file names in a list
path = input('\n'"Enter absolute path to directory: ")
filenames = os.listdir(path)
filenames.sort()
id_count = -1

# creates csv and adds desired headers
with open('manifest.csv', 'w', newline='') as csvfile:
    fieldnames = ['id','filename']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()

# writes file names and numbers to columns in csv.
    for filename in filenames:
        id_count += 1
        thewriter.writerow({'id':id_count, 'filename': filename})

print('\n'"Complete!")
