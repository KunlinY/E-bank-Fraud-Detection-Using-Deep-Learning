from pandas import read_csv

reader = read_csv('clean2.csv', chunksize=50001)

for chunk in reader:
    print(chunk)
