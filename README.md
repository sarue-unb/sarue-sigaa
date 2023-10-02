

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="sarue-UnB.png" alt="Logo" width="250" height="250">

  <h3 align="center">SARUE-SIGAA</h3>
</p>



<!-- ABOUT THE PROJECT -->
## About The Project
O SARUE-SIGAA é um sistema feito para fornecer funcionalidades extras ao módulo de extensão do SIGAA.

### Architecture
```
sarue-sigaa/
├─ main.py
├─ calculate_indicators/
│  ├─ calculate_all.py
│  ├─ calculate_members.py
│  ├─ calculate_objectives.py
│  ├─ calculate_qtd.py
│  ├─ calculate_status.py
│  ├─ dictionary_functions.py
│  ├─ sorted_dictionarys.py
├─ components/
|  ├─ database_formatter.py
|  ├─ info_printer.py
|  ├─ info_view.py
│  ├─ selection_components.py
├─ config/
│  ├─ ids/
│  │  ├─ actions_id_descryption.py
|  ├─ xapths
|  |  ├─ actions_xpath_descryption.py
|  ├─ actions_descryption.py
|  ├─ crawler_descryption.py
|  ├─ date_descryption.py
|  ├─ display_descryption.py
|  ├─ filter_descryption.py
|  ├─ json_descryption.py
|  ├─ libraries_descryption.py
|  ├─ output_format.py
|  ├─ url_descryption.py
├─ crawlers/
│  ├─ crawler_auth.py
│  ├─ crawler_config.py
│  ├─ crawler_data.py
│  ├─ type_search.py  
├─ database_generator/
│  ├─ database_generator.py
│  ├─ database_updater.py
│  ├─ json_generator.py
│  ├─ load_database.py
├─ databases/
│  ├─ base/
│  ├─ current/
│  ├─ history/
│  ├─ indicators/
├─ pages/
│  ├─ extension_pages.py
│  ├─ sigaa_pages.py
├─ tests/
│  ├─ auth_generator.py
│  ├─ data_generator.py
│  ├─ library_generator.py
│  ├─ url_generator.py
├─ README.md
├─ .env
├─ log.txt
├─ .gitignore
```

### Built With

* [Python](https://www.python.org/)
* [Selenium](https://selenium-python.readthedocs.io/)

<!-- GETTING STARTED -->
## Getting Started
Para rodar esse software é necessário ter o python3 instalado 

### Prerequisites
Before you can use this system, make sure you have the following prerequisites installed:

- **Python 3** 

### Prerequisites that will be installed by system
- **Selenium**
- **Dotenv**
- **Tqdm**

### Installation
- **Python 3** [Python Downloads](https://www.python.org/downloads/).



### Manual installation
- **pip:** pip is the package installer for Python. It is usually included with Python 3 installations. To verify if pip is installed, open your terminal or command prompt and run:

    ```bash
    pip --version
    ```

    If it's not installed, you can install it by following the instructions on the [pip installation guide](https://pip.pypa.io/en/stable/installation/).

  - **Selenium:**
  ```bash
  pip install selenium
  ```
  - **Dotenv:**
  ```bash
  pip install python-dotenv
  ```
  - **Tqdm:**
  ```bash
  pip install tqdm
  ```
  
<!-- USAGE EXAMPLES -->
## Usage
- Update base of sigaa actions:
`python main.py`
- Update storage of sigaa actions:
`python main.py REBASE`