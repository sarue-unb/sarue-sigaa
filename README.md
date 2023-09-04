

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
|  ├─ filter_descryption.py
|  ├─ json_descryption.py
|  ├─ output_format.py
|  ├─ url_descryption.py
├─ crawlers/
│  ├─ crawler_auth.py
│  ├─ crawler_data.py
│  ├─ type_search.py  
├─ database_generator/
│  ├─ database_generator.py
│  ├─ database_updater.py
│  ├─ json_generator.py
│  ├─ load_database.py
├─ databases/
│  ├─ current/
│  ├─ history/
│  ├─ indicators/
├─ pages/
│  ├─ extension_pages.py
│  ├─ sigaa_pages.py
├─ README.md
├─ .env
├─ .gitignore
```

### Built With

* [Python](https://www.python.org/)
* [Selenium](https://selenium-python.readthedocs.io/)

<!-- GETTING STARTED -->
## Getting Started
Para rodar esse software é necessário ter o python3 instalado 

### Prerequisites

- Python3
- Selenium
- Dotenv
- Tqdm
Please read this guide to understand how Selenium Xpath works https://www.guru99.com/xpath-selenium.html

### Installation
- pip install python-dotenv
- pip install selenium
- pip install tqdm

<!-- USAGE EXAMPLES -->
## Usage
`python main.py`
