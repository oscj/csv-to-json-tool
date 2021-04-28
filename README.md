# csv-to-json-tool

A simple python script to convert CSV files to JSON

## File format

We must ensure that the CSV file that we are trying to convert to JSON is in the proper format. Here are some guidelines for avoiding errors:

1. Make sure there is a column field name/header for each column of data. Make sure that these field names are snake cased and do not contain any commas. For example, if a column field name was 'Polymer Dosage', the correct name should be 'polymer_dosage'. This ensure consistency for when these JSON documents are inserted into the MongoDB database.

2. Ensure that the file does not contain any commas aside from the column/row delimiting commas that constitute a CSV file. For example, if there is a 'comments' field name, ensure that values for comments do not have commas within them.

## Using the script

This is the general execution call for the script:

``` bash
python3 csv_to_json.py <input_csv_path> <output_directory_path>
```

Please make sure that theses command line arguments are in the same order as above.
<br>

__Help Output__

By executing the help command of the script:

```bash 
 python3 csv_to_json.py --help
``` 

you will get the following:

```bash 
usage: csv_to_json.py [-h] path outdir

Convert a CSV file to JSON

positional arguments:
  path        The path of the CSV file to convert
  outdir      The path of the directory to save the JSON file

optional arguments:
  -h, --help  show this help message and exit
```
