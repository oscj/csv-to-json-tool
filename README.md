# csv-to-json-tool

A simple python script to convert CSV files to JSON

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
