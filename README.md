<h1 align="center">Data Anonymizer 💾</h1>
<p>
  <img src="https://img.shields.io/badge/python-v3-blue">
  <a href="https://github.com/curant/data-anonymizer/blob/master/LICENSE" target="_blank">
    <img alt="License: GPL--3.0" src="https://img.shields.io/badge/License-GPL--3.0-yellow.svg" />
  </a>
</p>

A Python module that anonymizes SQL dumps

#### Backstory

At my school, we always work on different types of projects once a year.
We built this tool in a team of 4. We realised how useful this tool can be and we decided to continue developing and publish it to our personal repositories.

## Requirements

* Python 3
* Pip
* MySQL (mysql, mysqldump)

## Installation

Install the Python module using pip

```sh
pip install .
```

## Usage

First we will need to generate a configuration file using the GUI.

```sh
python -m data_anonymizer -g -i dump.sql --host 127.0.0.1 --user root --pass toor --db anonymize
```

This will open a local webserver at <http://127.0.0.1:8000>, follow the instructions onscreen and download the configuration file.

Now we can create an anonymized SQL dump using the configuration file we just generated

```sh
python -m data_anonymizer -c config.yml -i dump.sql -o anonymized.sql
```

### Options

- `-h` Help

Command Line Interface (for anonymizing database)

- `-c <CONFIGFILE>` Configuration file
- `-i <INPUTFILE>` SQL dump file
- `-o <OUTPUTFILE>` SQL dump output anonymized

Graphical User Interface (for generating configuration file)

- `-g` GUI (starts Flask server)
- `--host <HOST>` Host of MariaDB/MySQL server
- `--user <USERNAME>` Username of MariaDB/MySQL server
- `--pass <PASSWORD>` Password of MariaDB/MySQL server
- `--db <DATABASE>` Temporary database

## Authors

👤 **Brady Renting**

* Github: [@bradyrenting](https://github.com/curant)

👤 **Redlolz**

* Github: [@Redlolz](https://github.com/Redlolz)

👤 **binari**

* Github: [@binari](https://github.com/binari)

👤 **Benjamin Roest**

* Github: [@benjaminroest](https://github.com/benjaminroest)

## Show your support

Give a ⭐️ if this project helped you!


## 📝 License

Copyright © 2020 [curant](https://github.com/curant).<br />
This project is [GPL-3.0](https://github.com/curant/data-anonymizer/blob/master/LICENSE) licensed.
