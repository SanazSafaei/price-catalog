# Price Catalog Serializer

Price Catalog Serializer is a Python program for dealing with csv files contain price of variations. It converts the data to 3 groups of Catalog fields, Articles and variation and represent the data as json file.

## Installation

For setup this project, you need to make a python virtualenv first and install requirements file. Run this command on you command-line.

```bash
pip install virtualenv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

For running tests in command line you can use this command:

```bash
coverage run -m unittest discover tests
```

For getting coverage reports you can run this command (you can also find the result on the end of this document) :
```bash
coverage report -m
#or
coverage html
```


## Usage

0. You can run program with default values with below command.

```bash
python3 main.py
```

1. Add your pricat.csv file in project directory or pass the file address as input argument with -f.
2. Add your mapping.csv file in project directory or pass the file address as input argument with -m.
3. If you want to combine multiple fields you need to add the field names in mappings.csv file with empty source and destination value. this is a sample of mapping.csv with customized field:

```
source;destination;source_type;destination_type
winter;Winter;season;season
;;price_buy_net|currency;
```

4.The default article id field is article_number, if you want to customize it you need to use -a flag.

5.The default result file name is json_price_catalog.json, if you want to customize it you need to use -j flag.

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
Here is the report of test coverage of current project.

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
- use csv library


## License

[MIT](https://choosealicense.com/licenses/mit/)