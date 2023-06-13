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

def parse_guidefile(guidefile):
    print("Parsing file:", guidefile.name)

    with open(guidefile.name) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    return soup

def extract_document_title(soup: BeautifulSoup):
    print("Extracting the guide's title")
    print(soup.title)

# Main program starts here.
if __name__ == '__main__':
    parser = argparse.ArgumentParser("duolingo-scraper", description='Extracts example sentences from Duolingo guides and converts it to Anki cards.')
    parser.add_argument("guide_file", help="Duolingo Guide file in HTML format.", type=argparse.FileType('r', encoding='latin-1'))
    args = parser.parse_args()

    soup = parse_guidefile(args.guide_file)
    extract_document_title(soup)
