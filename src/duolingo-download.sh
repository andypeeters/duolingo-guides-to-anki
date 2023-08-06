#!/bin/bash

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

# Takes in a single URL, downloads it and renames to the proper name.
# Parameter: $1 = single full URL.
# Output: string containing the original name of the file and the
#         renamed version.
process_url () {
    # Get the media file.
    wget "$1"

    # Remove all parts but the last one from the URL.
    duosource="$1"
    duofile=${duosource##*/}

    # Rename the file to the correct MP3.
    mv $duofile duolingo-$duofile.mp3

    # Print the new name.
    echo "$duofile ++ duolingo-$duofile.mp3"
}

# Main program starts below.

# The option '-f' signifies that an input file is provided.
if [ "$1" = "-f" ]
then
    echo "Processing input file: $2"

    # Read in the file contents.
    urlList=$(cat $2)
    
    # Store the processed items temporarily in an array.
    processedFiles=()

    # Process each line individually.
    for line in $urlList
    do
        result=$(process_url "$line")

        # Add new item to processed items.
        processedFiles+=("$result")
    done

    # Output all items of the array.
    for item in "${processedFiles[@]}"
    do
        echo $item
    done
else
    echo "Processing a single URL: $1"
    process_url "$1"
fi
