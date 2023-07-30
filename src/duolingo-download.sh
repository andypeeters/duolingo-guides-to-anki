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

# The option '-f' signifies that an input file is provided.
if [ "$1" = "-f" ]
then
    echo "Processing input file $2 containing several URL's..."

    # Read in the file contents.
    urlList=$(cat $2)
    
    # Store the processed items temporarily in an array.
    processedFiles=()

    # Process each line individually.
    for line in $urlList
    do
# TODO: Convert the file download code into a function,
# TODO: as it is the same code in the 'else' part.
# TODO: Must still be tested.

        # Get the media file.
        wget "$line"

        # Remove all parts but the last one from the URL.
        duosource="$line"
        duofile=${duosource##*/}

        # Rename the file to the correct MP3.
        mv $duofile duolingo-$duofile.mp3

        # Add new item to processed items.
        processedFiles+=("$duofile ++ duolingo-$duofile.mp3")
    done

    # Output all items of the array.
    for item in ${processedFiles[@]}
    do
        echo $item
    done
else
    echo "Processing a single URL..."

    # Get the media file.
    wget "$1"

    # Remove all parts but the last one from the URL.
    duosource="$1"
    duofile=${duosource##*/}

    # Rename the file to the correct MP3.
    echo $duofile
    echo duolingo-$duofile.mp3
    mv $duofile duolingo-$duofile.mp3
fi
