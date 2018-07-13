#!/usr/bin/python

import requests

from os import system
from sys import exit
from time import sleep



BASE_URL = 'http://www.geeksforgeeks.org/'
articles = []

def save_articles_as_html_and_pdf():
    print("All links scraped, extracting articles")
    # Formatting the html for articles
    all_articles = (
        '<!DOCTYPE html>'
        '<html><head>'
        '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
        '<link rel="stylesheet" href="style.min.css" type="text/css" media="all" />'
        '<script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script>'
        '</head><body>'
    )

    all_articles += '<h1 style="text-align:center;font-size:40px">' + \
                    category_url.title() + ' Archive</h1><hr>'
    all_articles += '<h1 style="padding-left:5%;font-size:200%;">Index</h1><br/>'

    for x in range(len(articles)):
        all_articles += '<a href =\"#' + str(x+1) + '\">' + \
                        '<h1 style="padding-left:5%;font-size:20px;">' + \
                        str(x+1) + ".\t\t"+articles[x].title + '</h1></a> <br/>'
    for x in range(len(articles)):
        all_articles += '<hr id=\"' + str(x+1) +'\">' + articles[x].content.decode("utf-8")

    all_articles += '''</body></html>'''
    html_file_name = 'G4G_' + category_url.title() + '.html'
    html_file = open(html_file_name, "w")
    html_file.write(all_articles.encode("utf-8"))
    html_file.close()

    pdf_file_name = 'G4G_' + category_url.title() + '.pdf'
    print("Generating PDF " + pdf_file_name)
    html_to_pdf_command = 'wkhtmltopdf ' + html_file_name + ' ' + pdf_file_name
    system(html_to_pdf_command)



if __name__ == '__main__':
    save_articles_as_html_and_pdf()
