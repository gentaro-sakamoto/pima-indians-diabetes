import csv

def loadCsv(filename):
  rows = csv.reader(open(filename, 'rb'))
  dataset = list(rows)
  for i in range(len(dataset)):
    dataset[i] = [float(x) for x in dataset[i]]

  return dataset

loadCsv('pima-indians-diabetes.csv')
