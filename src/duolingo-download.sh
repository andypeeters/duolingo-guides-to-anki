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

# Get the media file.
wget "$1"

# Remove all parts but the last one from the URL.
duosource="$1"
duofile=${duosource##*/}

# Rename the file to the correct MP3.
echo $duofile
echo duolingo-$duofile.mp3
mv $duofile duolingo-$duofile.mp3

