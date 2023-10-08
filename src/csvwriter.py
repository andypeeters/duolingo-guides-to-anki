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

import csv

class CsvWriter:
    """
    Class containing all methods to write all sentence records to an CVS file.
    """

    def __init__(self, output_file_name: str):
        """
        Initialiser.
        Opens the output file.

        output_file_name: str
            File name of the output file to write to.
        """

        self.__output_file = open(output_file_name, 'w', encoding='UTF8')
        self.__writer = csv.writer(self.__output_file, dialect='excel', delimiter='\t')

    def __del__(self):
        """
        Destructor.
        Closes the output file.
        """

        self.__output_file.close()

    def write_sentence_record(self, sentence: str, translation: str, guide_number: str, category_name: str):
        """
        Writes a full record to the output CSV file.

        sentence: str
            The original sentence.

        translation: str
            The translation added next to the original sentence.

        guide_number: str
            The number of the guide containing the example sentence.

        category_name: str
            The category name or heading of the paragraph containing the example sentence.
        """

        data_line = [sentence, translation, 'mp3', '[sound:mp3]', guide_number, category_name]
        self.__writer.writerow(data_line)
