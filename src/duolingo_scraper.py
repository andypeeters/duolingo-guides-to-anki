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
import csvwriter

def parse_guidefile(guidefile):
    print("Parsing file:", guidefile.name)

    with open(guidefile.name) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    return soup

def extract_document_guide_title(soup: BeautifulSoup):
    print("Extracting the guide's title...")
    items = soup.body.find_all('div', class_='_3LqTo')

    return items[0].get_text() if items else None

def extract_guide_number(guide_title: str):
    return re.search(r'Unit (\d+) Guidebook', guide_title).group(1)

def remove_newline_and_duplicate_spaces(textToClean: str):
    textToClean = textToClean.replace('\n', '')
    textToClean = " ".join(textToClean.split())

    return textToClean

def extract_category_title(keyPhrasesStartTag):
    print("Extracting category titles from the key phrases blocks...")
    if keyPhrasesStartTag.span:
        title = keyPhrasesStartTag.span.span.get_text()
        title = remove_newline_and_duplicate_spaces(title)
    else:
        title = None
    
    return title

def get_next_real_sibling(tag):
    tag = tag.next_sibling

    # Skip over any new line characters.
    while tag == '\n':
        tag = tag.next_sibling
    
    return tag

def process_sentence_record(writer: csvwriter.CsvWriter, sentence_block_tag, category_name: str):
    if sentence_block_tag is None:
        return False

    sentence_tag = sentence_block_tag.find('div', class_='ZBgAa')
    if sentence_tag:
        sentence = sentence_tag.span.span.get_text()
    else:
        # End further processing of the block as no sentence value is present.
        return False

    translation_tag = sentence_block_tag.find('div', class_='_1F4vM')
    if translation_tag:
        translation = translation_tag.span.span.get_text()
        translation = remove_newline_and_duplicate_spaces(translation)

    writer.write_sentence_record(sentence, translation, guide_number, category_name)
    return True

def extract_sentence(writer: csvwriter.CsvWriter, startTag, category_name: str, guide_number: str):
    print("Extracing sentences from phrase block...")
    possible_sentence_tag = startTag;

    while possible_sentence_tag != None:
        possible_sentence_tag = get_next_real_sibling(possible_sentence_tag)
        if possible_sentence_tag is None:
            break
        
        possible_sentence_tag = get_next_real_sibling(possible_sentence_tag)
        if possible_sentence_tag is None:
            break

        cleaned_possible_sentence_tag_contents = [x for x in possible_sentence_tag.contents if x != '\n']
        total_sentences_in_block = len(cleaned_possible_sentence_tag_contents)
        print("Number of sentences to extract: ", total_sentences_in_block)

        # Loop over the counted number of sentences.
        for i in range(0, total_sentences_in_block):
            sentence_block_tag = cleaned_possible_sentence_tag_contents[i].div
            keepGoing = process_sentence_record(writer, sentence_block_tag, category_name)
        
            # If no sentence could be written, end the for and while loops.
            if not keepGoing:
                return

def select_second_next_block_tag(startTag):
    # The following function jumps 2 tags ahead.
    category_tag = get_next_real_sibling(startTag)
    category_tag = get_next_real_sibling(category_tag)
    return category_tag

def search_for_key_phrase_blocks(soup: BeautifulSoup, output_file_name: str, guide_number: str):
    print("Searching for the key phrases blocks...")
    searchtext = re.compile('KEY(.*)PHRASES', re.DOTALL)
    parents = soup.body.find_all('div', class_='_1WCLL')

    writer = csvwriter.CsvWriter(output_file_name)

    for tag in parents:
        child = tag.find('span', string=searchtext)
        if child:
            category_tag = select_second_next_block_tag(tag)
            category_title = extract_category_title(category_tag)
            if category_title:
                extract_sentence(writer, category_tag, category_title, guide_number)
    
    del writer

# Main program starts here.
if __name__ == '__main__':
    parser = argparse.ArgumentParser("duolingo-scraper", description='Extracts example sentences from Duolingo guides and converts it to Anki cards.')
    parser.add_argument("guide_file", help="Duolingo Guide file in HTML format.", type=argparse.FileType('r', encoding='latin-1'))
    args = parser.parse_args()

    soup = parse_guidefile(args.guide_file)
    guide_title = extract_document_guide_title(soup)
    if guide_title:
        print('Processing:', guide_title)
        guide_number = extract_guide_number(guide_title)
        output_file_name = guide_title.replace(' ', '_') + '.csv'
        search_for_key_phrase_blocks(soup, output_file_name, guide_number)
    else:
        print('No proper title was found, this might mean that the file hasn\'t the expected structure.')
