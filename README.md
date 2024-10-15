# Text-to-Speech (TTS) Document Reader

This Python project reads text from various document formats (.txt, .pdf, .docx) and converts it to speech using the `pyttsx3` library. The spoken output can be saved as an audio file in MP3 format.

## Features

- Reads text from `.txt`, `.pdf`, and `.docx` files.
- Converts the extracted text into speech.
- Saves the audio output as an MP3 file with a unique filename to avoid overwriting.

## Requirements

- Python 3.x
- `pyttsx3` library for text-to-speech conversion
- `PyPDF2` library for reading PDF files
- `python-docx` library for reading DOCX files

You can install the required libraries using pip:

```bash
pip install pyttsx3 PyPDF2 python-docx
