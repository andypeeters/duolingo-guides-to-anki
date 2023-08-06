# Description On Using `duolingo-download.sh`

The `duolingo-download.sh` script has been extended to be able to download multiple files in one go.

## Syntax

Depending on the requirement to download only 1 audio file or multiple ones, the following syntax must be used:

- Single file download: `duolingo-download.sh <URL>`
- Multiple file download: `duolingo-download.sh -f <input file>`

The `<input file>` is a simple text file containing several URL's with each URL on a separate new line.

## Collecting the URL's

1. Surf in the brower to the guide within Duolingo wanting to download the audio from.
2. Open up the Developer tools by pressing F12 and select the tab **Network**.
3. Click the play icon of an example sentence, look up the corresponding URL in the **Network** tab and copy the URL value.
4. Paste the copied URL into a text file on a separate line (!).
5. Follow the steps 3 and 4 to collect the URL's for each remaining audio file.

## Download the Audio Files

In case of downloading multiple audio files, save the created text file, e.g. _duolingo-audio-to-download.txt_, and run the command:

```sh
duolingo-download.sh -f duolingo-audio-to-download.txt
```

After downloading all files, the script will print out all new file names to the console output.

Downloading a single audio file can be done using this command:

```sh
duolingo-download.sh https://host/to/duolingo/audiofile/guid
```

Also here, the script will print out the new file name to the console output.

## Store File Names In CSV

Take the local file name(s) of the audio file(s) from the console output and copy it/them into the placeholder field(s) of the generated CSV file from the `duolingo_script.py` execution.

Pay close attention which audio file name goes to which line to make sure the audio and sentences match up.
