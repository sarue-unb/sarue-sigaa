

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SAIe-SIGAA</h3>

  <p align="center">
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- ABOUT THE PROJECT -->
## About The Project
O SAIe-SIGAA é um sistema feito para fornecer funcionalidades extras ao módulo de extensão do SIGAA.

### Architecture
```
saie-sigaa/
├─ main.py
├─ crawler.py
├─ components/ ## Reusable components
│  ├─ selection_components.py
├─ pages/ # Each page is separated into a different domain
│  ├─ extension_page.py
│  ├─ sigaa_page.py
├─ README.md
├─ .env
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
