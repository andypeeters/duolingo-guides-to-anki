**Note** This repository is archived due to a very simple reason: I don't need these scripts anymore. To avoid
any (potential) maintenance issues, I close this repository but will still keep it around for any future
reference if necessary.

# Duolingo Guides to Anki

This project contains a collection of scripts to scrape example sentences and audio from the Duolingo Guides
and convert them into Anki cards.

## Description

Since the latest update of Duolingo to the learning path, they added guides to (several) units. Those guides
contain example senctences to show new words and explain new grammer points of the language.

As everyone knows, Duolingo on its own is rarely enough to learn a language. And as such having those example
sentences in an Anki deck, as a first step, would be very useful to get some extra repetition of words and
sentences.

### Goals and Technology

The main goal was to write the necessary scripts to get the sentences converted in Anki cards without too
much manual work.

A second goal I had, was to write the scripts in a programming language that has as little friction as possible
to start with. In the end I came to the conclusion that Python would be a good choice. Because I have never
written program in Python before, using it for this project allowed me get experience with an additional language
and platform, and broaden your horizon in tech is never really a bad thing.

## Features

At the moment there are 2 scripts:

1. **duolingo-download.sh** is used to download the audio of each example sentence.
2. **duolingo_scraper.py** extracts the examples sentences and converts the data into a CSV file.
    The other ***.py** files provide extra functionality for the main script.

### CSV File Format

Every line in the CSV file has the following structure:

1. The original sentence (in the language being learned)
2. The translated sentence (in the language of the UI)
3. Fixed value 'mp3'. Placeholder value for later use.
4. Fixed value '[sound:mp3]'. Another placeholder value for later use.
5. The guide number.
6. The title of the example sentence block.

Each field is separated by tabs.

### Limitations

First and foremost: the code of the python script is not so good, to say the least, to not to say it is kind of
crap. But it works for what it needs to do. I have the intention to improve the code quality but that will be for
later versions.

The scraper cannot download the audio files (for now). That's why a separate script is needed. Additionally, to let the scraper
do its job, it needs a local copy of the guide. In other words, it is necessary to save a Duolingo guide to local
disk first, and then run the scraper on that file.

Next versions of the script(s) will attempt to remove these limitations.

## Installation

Just copy the scripts (include all ***.py** files) into a directory of your choice. And in case of Linux/Unix execute the following command
to make the scripts executable:

`chmod u+x duolingo-download.sh duolingo_scraper.py`

### Requirements

The following software must be available on your computer to be able to run the scripts:

- Bash shell, `cat`, and `wget`.
- Python 3.

## Usage

1. First, open Duolingo in a browser, open the guide and save it to local disk. It is not needed to save all files,
   just the main HTML page is sufficient.
2. Open up a terminal window.
3. Run the scraper with the following command: `python duolingo_scraper.py /path/to/local-file.html`

The usage steps of the downloader script are available here: [Description On Using `duolingo-download.sh`](docs/downloadscript.md)

After completing all steps, import the CSV file into Anki and move all audio files the media collection of the Anki
profile.

## How to Contribute

For the moment, there are no guidelines on how to contribute. Open a GitHub Issue when you have a question,
comment or remark. Or just to start a conversation about the project.

## License

GNU General Public License v3.0 or later

See **[LICENSE](LICENSE)** to see the full text.

## Changelog

- v1.0.0: first packaged release.
- v1.1.0: improved `duolingo-download.sh` script.
- v1.2.0: refactored some code in the `duolingo_scraper.py` script and fix a scraper bug.
