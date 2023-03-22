import pandas as pd
import requests as requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import copy
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import _excel as excel

df = pd.read_csv('D:\pythonProject\data_file\Covid19Vaccine.csv')
print(df)
# df.head()
# cojs_dict = df.to_dict()