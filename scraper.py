from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/abhin/Downloads/chromedriver_win32 (1)/chromedriver")
browser.get(starturl)
time.sleep(10)

def scrape():
    headers = ["Name", "LightyearsFromEarth",  "PlanetMass", "StellarMagnitude", "DiscoveryDate"]
    planetData = []
    for i in range(0, 10):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for l in soup.find_all("ul", attrs = {"class", "exoplanet"}):
            litags = l.find_all("li")
            tempList = []
            for index, litag in enumerate(litags):
                if index == 0:
                    tempList.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        tempList.append(litag.contents[0])
                    except:
                        tempList.append("")
            planetData.append(tempList)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("Planets.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetData)

scrape()