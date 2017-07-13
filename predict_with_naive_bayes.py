import pprint
import csv
import random
import math

csvFileName = 'pima-indians-diabetes.csv'

def loadCsv(filename):
  rows = csv.reader(open(filename, 'r'))
  dataset = list(rows)
  for i in range(len(dataset)):
    dataset[i] = [float(x) for x in dataset[i]]
  return dataset

def splitDataset(dataset, splitRatio):
  trainSize = int(len(dataset) * splitRatio)
  trainSet = []
  copiedDataSet = list(dataset)
  while len(trainSet) < trainSize:
    index = random.randrange(len(copiedDataSet))
    trainSet.append(copiedDataSet.pop(index))
  return [trainSet, copiedDataSet]

def separateByClass(dataset):
  separated ={}
  for i in range(len(dataset)):
    verctor = dataset[i]
    classValue = verctor[-1]
    if (classValue not in separated):
      separated[classValue] = []
    separated[classValue].append(verctor)
  return separated

def mean(numbers):
  return sum(numbers) / len(numbers)

def stdev(numbers):
  avg = mean(numbers)
  variance = sum([pow(x - avg, 2) for x in numbers])
  return math.sqrt(variance)

nums = [1,1,1,1,1]
nums2 = [10,1,5,1,1]
print(stdev(nums))
print(stdev(nums2))
