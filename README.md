## Description

Automation script to register products on the [DLP Hashtag Treinamentos system](https://dlp.hashtagtreinamentos.com/python/intensivao/login) using Python, [PyAutoGUI](https://pyautogui.readthedocs.io/) for GUI interaction, and [Pandas](https://pandas.pydata.org/) to read product data.

This project is part of the Python automation exercises from Hashtag Treinamentos' Intensivão Python course.

## Requirements to run the script

- Install Python 3.8+
- Install the required libraries:
  ```bash
  pip install pyautogui pandas openpyxl
  ```

Have a browser installed (Opera, Chrome, Edge, etc.)
Have a CSV file with the following columns (in this exact order):
codigo
marca
tipo
categoria
preco_unitario
custo
obs (optional — can be empty or missing in some rows)

produtos.csv is just an example file. You can use any CSV file with the same column names. Just change the filename in the script:Pythontabela = pd.read_csv("seu_arquivo_aqui.csv")
Important: This is GUI-based automation (pixel coordinates). It is sensitive to:
Screen resolution
Browser zoom level
Window position/size
Taskbar height
Run it in the same environment used for testing.

Installation
Bash# Clone or download the project
git clone <your-repo-url>
cd hashtag-python-automation

# Install dependencies

pip install pyautogui pandas openpyxl

# or use a requirements.txt if you have one:

# pip install -r requirements.txt

Running the script

Prepare your CSV file (any name, as long as columns match)
Open the script (cadastro_produtos.py or similar) and update these lines if needed:Pythontabela = pd.read_csv("produtos.csv") # ← change to your filename here

# ...

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.write("sua senha") # ← change password or use input()
Make sure the browser is closed before running
Execute:

Bashpython cadastro_produtos.py
The script will:

Open the browser
Go to the login page
Perform login
Read your CSV file
Register each product by filling the form

Security note: The password is hardcoded in the example. For real use, replace it with:Pythonsenha = input("Enter your password: ")
pyautogui.write(senha)or use environment variables / .env file.
How it works (quick overview)
Pythonimport pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

# Open browser → login → read ANY csv file → loop and fill form for each row

tabela = pd.read_csv("produtos.csv") # ← this can be qualquer_arquivo.csv
Tips & Improvements

Find new coordinates with: print(pyautogui.position()) while hovering the mouse
Add screenshots for debug: pyautogui.screenshot("debug.png")
Handle errors with try/except blocks
For more reliable automation → consider migrating to Selenium or Playwright
Support other file types (Excel, etc.):Python# Example for .xlsx
tabela = pd.read_excel("produtos.xlsx")

Project structure example
texthashtag-python-automation/
├── cadastro_produtos.py # main automation script
├── produtos.csv # example data file (you can use any .csv)
├── meu_estoque_2025.csv # your real file (change name in code)
├── requirements.txt
└── README.md
Good automation! 🐍📊
Made with ❤️ following Hashtag Treinamentos Python Intensivão challenges.
textAgora está bem explícito que o arquivo pode ser qualquer um, desde que tenha as colunas corretas. Se quiser mais ajustes (ex: seção de "Customizing the script", exemplos de outros nomes de arquivo, ou algo mais), me avise!1.3sFast
