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
import csv

def parse_guidefile(guidefile):
    print("Parsing file:", guidefile.name)

    with open(guidefile.name) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    return soup

def extract_document_guide_title(soup: BeautifulSoup):
    print("Extracting the guide's title...")
    items = soup.body.find_all('div', class_='_3LqTo')

    return items[0].get_text() if items else None

def extract_category_title(keyPhrasesStartTag):
    print("Extracting category titles from the key phrases blocks...")
    title = keyPhrasesStartTag.span.span.get_text()
    return title

def extract_sentence(writer, startTag, category_name: str):
    print("Extracing sentences from phrase block...")
    possible_sentence_tag = startTag;

    while possible_sentence_tag != None:
        possible_sentence_tag = possible_sentence_tag.next_sibling
        if possible_sentence_tag is None:
            break
        
        possible_sentence_tag = possible_sentence_tag.next_sibling
        if possible_sentence_tag is None:
            break

        sentence_block_tag = possible_sentence_tag.div
        if sentence_block_tag is None:
            break

        sentence_tag = sentence_block_tag.find('div', class_='ZBgAa')
        if sentence_tag:
            sentence = sentence_tag.span.span.get_text()
        else:
            # End further processing of the block as no sentence value is present.
            break

        translation_tag = sentence_block_tag.find('div', class_='_1F4vM')
        if translation_tag:
            translation = translation_tag.span.span.get_text()
    
        data_line = [sentence, translation, 'mp3', '[sound:mp3]', 0, category_name]
        writer.writerow(data_line)

def search_for_key_phrase_blocks(soup: BeautifulSoup, output_file_name: str):
    print("Searching for the key phrases blocks...")
    searchtext = re.compile('KEY(.*)PHRASES', re.DOTALL)
    parents = soup.body.find_all('div', class_='_1WCLL')

    with open(output_file_name, 'w', encoding='UTF8') as csv_file:
        writer = csv.writer(csv_file, dialect='excel', delimiter='\t')

        for tag in parents:
            child = tag.find('span', string=searchtext)
            if child:
                category_tag = tag.next_sibling.next_sibling
                category_title = extract_category_title(category_tag)
                extract_sentence(writer, category_tag, category_title)

# Main program starts here.
if __name__ == '__main__':
    parser = argparse.ArgumentParser("duolingo-scraper", description='Extracts example sentences from Duolingo guides and converts it to Anki cards.')
    parser.add_argument("guide_file", help="Duolingo Guide file in HTML format.", type=argparse.FileType('r', encoding='latin-1'))
    args = parser.parse_args()

    soup = parse_guidefile(args.guide_file)
    guide_title = extract_document_guide_title(soup)
    if guide_title:
        print('Processing:', guide_title)
        output_file_name = guide_title.replace(' ', '_') + '.csv'
        search_for_key_phrase_blocks(soup, output_file_name)
    else:
        print('No proper title was found, this might mean that the file hasn\'t the expected structure.')
