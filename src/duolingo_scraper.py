# Copyright (c) 2023, Andy Peeters <andy@studiopasokon.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program, see LICENSE.
# If not, see <https://www.gnu.org/licenses/gpl-3.0.txt>.

import argparse
from bs4 import BeautifulSoup
import re

def parse_guidefile(guidefile):
    print("Parsing file:", guidefile.name)

    with open(guidefile.name) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    return soup

# HACK: Temporary test function, may be removed later.
def extract_document_title(soup: BeautifulSoup):
    title = soup.head.title.get_text()
    print("Extracting the guide's title:", title)
    return title

def extract_document_guide_title(soup: BeautifulSoup):
    print("Extracting the guide's title...")
    items = soup.body.find_all('div', class_='_3LqTo')

    return items[0].get_text() if items else None

def extract_category_title(soup: BeautifulSoup, keyPhrasesStartTag):
    print("Extracting category titles from the key phrases blocks...")
    category_title_tag = keyPhrasesStartTag.next_sibling.next_sibling
    if category_title_tag:
        title = category_title_tag.span.span.get_text()
        return title

def search_for_key_phrase_blocks(soup: BeautifulSoup):
    print("Searching for the key phrases blocks...")
    searchtext = re.compile('KEY(.*)PHRASES', re.DOTALL)
    parents = soup.body.find_all('div', class_='_1WCLL')

    for tag in parents:
        child = tag.find('span', string=searchtext)
        if child:
            category_title = extract_category_title(soup, tag)
            print(category_title)

# Main program starts here.
if __name__ == '__main__':
    parser = argparse.ArgumentParser("duolingo-scraper", description='Extracts example sentences from Duolingo guides and converts it to Anki cards.')
    parser.add_argument("guide_file", help="Duolingo Guide file in HTML format.", type=argparse.FileType('r', encoding='latin-1'))
    args = parser.parse_args()

    soup = parse_guidefile(args.guide_file)
    guide_title = extract_document_guide_title(soup)
    if guide_title:
        print(guide_title)

    search_for_key_phrase_blocks(soup)
