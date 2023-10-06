# Scraper example. Pulls information from nature.com. User defines the number of pages
# that are searched and the article types that are scraped.

import os
import requests
import string

from bs4 import BeautifulSoup

num_pages = int(input())
target_article_type = input()

base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"
article_filenames = []

for page_number in range(1, num_pages + 1):
    os.makedirs(f"Page_{page_number}", exist_ok=True)

    response = requests.get(base_url + f"&page={page_number}")
    soup = BeautifulSoup(response.text, "html.parser")

    if not response:
        print(f"The URL returned {response.status_code}")
    else:
        article_list = soup.find_all("article")

        for list_item in article_list:
            article_type = list_item.find("span", attrs={"data-test": "article.type"}).text
            if article_type == target_article_type:
                article_path = list_item.find('a', attrs={"data-track-action": "view article"})["href"]
                response = requests.get(f"https://www.nature.com{article_path}")
                soup = BeautifulSoup(response.text, "html.parser")

                article_name = soup.find("title").text
                article_filename = article_name.strip(string.punctuation).replace(' ', '_') + ".txt"
                article_filenames.append(article_filename)

                article_content = soup.find('p', attrs={"class": "article__teaser"}).text

                os.chdir(f"Page_{page_number}")
                with open(article_filename, "w", encoding='utf-8') as file:
                    file.write(article_content)
                os.chdir("..")

    print(article_filenames)
