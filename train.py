import csv
import os


# Construct the path to the dataset
inputs_dir = os.getenv('VH_INPUTS_DIR', '')
dataset_file = os.path.join(inputs_dir, 'dataset', 'dataset.csv')


print('Printing dataset contents')
with open(dataset_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
