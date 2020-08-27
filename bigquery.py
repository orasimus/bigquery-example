import argparse
import csv
import os

from google.cloud import bigquery


# Parse the BigQuery table argument
parser = argparse.ArgumentParser()
parser.add_argument('--bigquery-table', type=str, required=True)
args = parser.parse_args()


print('Creating a BigQuery query')
client = bigquery.Client()

query = f"""
    SELECT *
    FROM {args.bigquery_table}
"""

print('Executing the query')
response = list(client.query(query))


print('Transforming results')
header = [response[0].keys()]
rows = list(map(lambda row: row.values(), response))
csv_content = header + rows


# Construct the path to write the dataset
output_dir = os.getenv('VH_OUTPUTS_DIR', '')
dataset_filename = os.path.join(output_dir, 'dataset.csv')

print(f'Writing results to {dataset_filename}')
with open(dataset_filename, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_content)
