import requests
from pyquery import PyQuery as pq
import csv

URL = "https://de.wikipedia.org/wiki/Elyas_M%E2%80%99Barek"
page = requests.get(URL)

d = pq(page.text)
filme = ("#mw-content-text > div.mw-parser-output > div:nth-child(13) > ul:nth-child(2) > li")
with open("mbarek.csv", "w") as f:
	writer = csv.writer(f, delimiter=";")
	writer.writerow(["titel", "jahr", "url"])
	for film in d(filme).items():
		titel = film.text().split(": ")[1]
		jahr = film.text().split(": ")[0]
		url = film.find("a").attr("href")
		writer.writerow([titel, jahr, url])
