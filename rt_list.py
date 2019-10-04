#!/usr/bin/env python3
"""
Script to take RottenTomatoes TOP ### list and generate a CSV that can be
imported into Letterboxd

Usage: rt_list.py <RT List URL> > output.csv
"""

import argparse
import csv
import time
import os
import re
import requests
import urllib
from bs4 import BeautifulSoup


def add_movie(name, year, args):
    global movie_list

    # Escape name if it contains commas
    if "," in name:
        name = '"' + name + '"'

    # Remove parenthesized content
    # Sometimes the original name of the movie is in parenthesis
    if args.leave_parenthesis is False:
        name = re.sub(r"\(.*\)", "", name).strip()

    movie_list.append((name, year))


def process_html(html, args):
    soup = BeautifulSoup(html, "html.parser")

    for item in soup.find_all("div", {"class": "article_movie_title"}):
        add_movie(item.a.contents[0], item.span.contents[0].strip("()"), args)

    # Reverse order since RT usually starts with the lowest ranked and goes up
    if args.no_reverse is False:
        movie_list.reverse()

    # Print csv header!
    print("Title,Year")

    # Print the rest of the items
    for movie, year in movie_list:
        print(",".join([movie, year]))


parser = argparse.ArgumentParser()
parser.add_argument("--no_reverse", action="store_true", help="Don't the list order")
parser.add_argument(
    "--leave_parenthesis",
    action="store_true",
    help="Don't remove content in parenthesis from title",
)
parser.add_argument("url", help="url")
args = parser.parse_args()

movie_list = []

request = requests.get(args.url)
if request is not None:
    process_html(request.content, args)
