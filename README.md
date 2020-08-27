# Valohai BigQuery Example

This is an example of a 2 step Valohai pipeline, which queries data from BigQuery and "trains a model".

The first step queries data from BigQuery and stores a snapshot of the data at current time.

The second step uses this data snapshot to "train a model", in reality just printing out the dataset contents.

## Running the Example

Easiest way of running the example is by forking this repository, following the requirements below and connecting the fork to a Valohai project.

Another way is to clone the repository and then use [valohai-cli](https://github.com/valohai/valohai-cli/) to run the steps as adhoc executions one after the other.

In order to run the example, you must:

(1)  
Have a Google Cloud project with a BigQuery dataset.

(2)  
Edit the `valohai.yaml` file, changing the default value of the `bigquery-table` parameter to the name of a table in your BigQuery dataset.

Optionally, edit the query in `bigquery.py`.

(3)  
In the Google Cloud project, create a Service account with the BigQuery Admin role and create a JSON key for the account: https://cloud.google.com/bigquery/docs/reference/libraries#setting_up_authentication

Upload this key into your Valohai project, in Project -> Data -> Upload.

From Project -> Data -> Browse, copy the datum address of the uploaded key.

Edit the `valohai.yaml` file, changing the default value of the `credentials` input to the datum address that you copied.
