#How do the flight phases (ex. take off, cruise, landing..) contribute to fatalities? Chart!

import csv
import webget
import requests

url = 'https://raw.githubusercontent.com/edipetres/Depressed_Year/master/Dataset_Assignment/AviationDataset.csv'
requests.get(url, params={'downloadformat' : 'csv'})