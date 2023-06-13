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

### Limitations

(still to add)

## Installation

Just copy the scripts into a directory of your choice. And in case of Linux/Unix execute the following command
to make the scripts executable:

`chmod u+x duolingo-download.sh duolingo-scraper.py`

### Requirements

The following software must be available on your computer to be able to run the scripts:

- Bash shell, and the wget tool.
- Python 3.

## Usage

(still to add)

## How to Contribute

For the moment, there are no guidelines on how to contribute. Open a GitHub Issue when you have a question,
comment or remark. Or just to start a conversation about the project.

## License

GNU General Public License v3.0 or later

See `LICENSE <LICENSE>`_ to see the full text.
