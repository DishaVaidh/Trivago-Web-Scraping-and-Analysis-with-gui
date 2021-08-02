# Trivago-Web-Scraping-and-Analysis-with-gui
## Description
In this tkinter based gui project, data of trivago website is first extracted for a particular city of 1 year and then analyse the data.First the city name is automatically entered,then it selects filters by automation for selecting stars(1 star,2 star,3 star,4 star,5 star) and air conditioning.The extracted data are Hotel name,Rate,checkin date,checkout date,booking site and distance.Then the data extracted is used for analysing which hotels have highest rates by ploting a graph.



## Skills used
Web scraping - Selenium, Python
Data Analysis - Python, Pandas, Plot.ly
Gui Programming - Tkinter



## system requirements
windows 7
Python 3.6.5
60GB HDD
2 GB RAM
Chrome Browser



## Installations
python -m pip install numpy
python -m pip install pandas
python -m pip install selenium
python -m pip install webdriver_manager
python -m pip install plotly
python -m pip install pyinstaller

## Deploy to exe
pyinstaller.exe --hidden-import babel.numbers trivago_tk.py



