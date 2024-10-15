import os
import pyttsx3
import PyPDF2
import docx

# Initialize the TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female
engine.setProperty('rate', 165)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to read text from a .txt file
def read_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to read text from a .pdf file
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

# Function to read text from a .docx file
def read_docx(file_path):
    doc = docx.Document(file_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

# Function to read file based on the extension
def read_document(file_path):
    if file_path.endswith('.txt'):
        return read_txt(file_path)
    elif file_path.endswith('.pdf'):
        return read_pdf(file_path)
    elif file_path.endswith('.docx'):
        return read_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please use a .txt, .pdf, or .docx file.")

# Function to generate a unique filename
def get_unique_filename(base_filename):
    counter = 1
    filename, extension = os.path.splitext(base_filename)
    new_filename = base_filename

    while os.path.exists(new_filename):
        new_filename = f"{filename}_{counter}{extension}"
        counter += 1

    return new_filename

# Define the file path for the document you want to read
file_path = 'C:/Users/merwi/OneDrive/Documents/intro speech.docx'  # Change this to your file's path

# Extract text from the document
text = read_document(file_path)

# Convert text to speech and save it to a file
output_filename = 'speech_output.mp3'
unique_filename = get_unique_filename(output_filename)

# Speak the text and save it
engine.say(text)
engine.save_to_file(text, unique_filename)
engine.runAndWait()

print(f"Audio saved as: {unique_filename}")
