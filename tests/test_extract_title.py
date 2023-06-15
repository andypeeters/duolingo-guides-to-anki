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

from bs4 import BeautifulSoup
import unittest

import os
import sys
script_dir = os.path.dirname( __file__ )
module_dir = os.path.join(script_dir, '..', 'src')
sys.path.append(module_dir)

import duolingo_scraper as scraper

class Test_TestHtmlExtration(unittest.TestCase):
    def test_extract_title(self):
        soup = BeautifulSoup('<html><head><title>Basic title</title></head><body>No body.</body></html>', 'html.parser')
        self.assertEqual(scraper.extract_document_title(soup), 'Basic title')

if __name__ == '__main__':
    unittest.main()
