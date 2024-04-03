# Price Catlog Serializer

Price Catlog Serializer is a Python program for dealing with csv files contain price of variations. It converts the data to 3 groups of Catlog fields, Articles and vaiation and represent the data as json file.

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
1. add your pricat.csv file in project directory.
2. add your mapper.csv file in project directory.
3. if you have customize field add your json_config.csv file in project directory.
4. run command below,

```bash
python3 main.py
```

## Test Section
Here is the report of test converage of current project.

| Name                             |    Stmts |     Miss |   Cover |
|--------------------------------- | -------: | -------: | ------: |
| article.py                       |        9 |        0 |    100% |
| catalog.py                       |        8 |        0 |    100% |
| convert\_to\_json.py             |       15 |        0 |    100% |
| file\_manager.py                 |       28 |        4 |     86% |
| grouper.py                       |       39 |        0 |    100% |
| mapper.py                        |       24 |        0 |    100% |
| price\_catalog.py                |       32 |        0 |    100% |
| tests/test\_convert\_to\_json.py |       24 |        0 |    100% |
| tests/test\_file\_manager.py     |       19 |        1 |     95% |
| tests/test\_grouper.py           |       40 |        0 |    100% |
| tests/test\_mapper.py            |       26 |        0 |    100% |
| tests/test\_price\_catalog.py    |       30 |        0 |    100% |
|                        **TOTAL** |  **294** |    **5** | **98%** |

## License

[MIT](https://choosealicense.com/licenses/mit/)