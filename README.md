# Price Catalog Serializer

Price Catalog Serializer is a Python program for handling CSV files containing the price of variations. It converts the data into three groups of Catalog fields, Articles, and Variations and represents the data as a JSON file.

## Installation

To set up this project, you need to make a python virtualenv first and install the requirements file. Run this command on your command-line.To set up this project, you should create a Python virtual environment first and install the required packages by running the command provided in the terminal.

```bash
pip install virtualenv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

For running tests in the command line you can use this command:

```bash
coverage run -m unittest discover tests
```

Here's the command to run for coverage reports (also available at the end of the document):

```bash
coverage report -m
#or
coverage html
```


## Usage

0. To run the program with the default values, use the command below.

```bash
python3 main.py
```

To use this tool, you need to follow these three steps:

1. First, you must specify the file address as an input argument using the -f option. Alternatively, you can override the pricat.csv file in the sample directory.

2. Next, specify the file address as an input argument using the -m option. Again, you can override the pricat.csv file in the sample directory.

3. If you want to combine multiple fields, you need to add the corresponding field names in the mapping.csv file. Please note that you should leave the source and destination values blank for the customized field. Here's an example of mapping.csv with a customized field:

```
source;destination;source_type;destination_type
winter;Winter;season;season
;;price_buy_net|currency;
```

4. The default article id field is "article_number". If you want to customize it, you need to use the -a flag. 

5. The default result file name is "json_price_catalog.json". If you want to customize it, you need to use the -n flag.

```bash
python3 run.py --help

usage: run.py [-h] [-f FILE_PATH] [-m MAPPER_PATH] [-a ARTICLE_id] [-n JSON_FILE_NAME]

Process catalog csv data and convert it to json file.

options:
  -h, --help            show this help message and exit
  -f FILE_PATH, --filename FILE_PATH
                        Path of data file. sample /dir/pricat.csv
  -m MAPPER_PATH, --mapper MAPPER_PATH
                        Path of mapping file. sample /dir/mapping.csv
  -a ARTICLE_id, --article_id ARTICLE_id
                        Path of mapping file. sample article_id
  -n JSON_FILE_NAME, --json_file_name JSON_FILE_NAME
                        Path of mapping file. sample json_response
```

## Test Section
Here is the report of test coverage of the current project.

| Name                             |    Stmts |     Miss |   Cover |
|--------------------------------- | -------: | -------: | ------: |
| src/convert\_to\_json.py         |       15 |        0 |    100% |
| src/dto/article.py               |        9 |        0 |    100% |
| src/dto/catalog.py               |        8 |        0 |    100% |
| src/file\_manager.py             |       28 |        4 |     86% |
| src/grouper.py                   |       39 |        0 |    100% |
| src/mapper.py                    |       41 |        0 |    100% |
| src/price\_catalog.py            |       33 |        0 |    100% |
| tests/test\_convert\_to\_json.py |       24 |        0 |    100% |
| tests/test\_file\_manager.py     |       17 |        0 |    100% |
| tests/test\_grouper.py           |       40 |        0 |    100% |
| tests/test\_mapper.py            |       26 |        0 |    100% |
| tests/test\_price\_catalog.py    |       30 |        0 |    100% |
|                        **TOTAL** |  **310** |    **4** | **99%** |


## Next Steps:

- Read and process each data line separately for better in-memory performance for large files
- use CSV library


## License

[MIT](https://choosealicense.com/licenses/mit/)