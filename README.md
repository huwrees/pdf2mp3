# pdf2mp3



## Future Work

### Suggestions
* .gitignore - venv, ...
* Add to github repo
* Helpful function = os walk function. It'll recursively iterate through every file in a directory. From there, in your loop you could check the file extension and remove based on that or any other condition. 
* You could use the argparse package and take arguments from the cli to ask the user things like what files they want to remove or the file extensions they want to remove. 
* You could think about putting everything in functions so as to not pollute the global namespace and use the standard "if _name_ == '__main__'" pattern.

#### Example Improvement
When trying the first one, I had to spend quite a lot of time debugging, possibly due to the fact that the used modules have been updated since the video has been made and a number of functions had been renamed (even ChatGPT is not updated regarding PyPDF2 3.0.0 !). If you wish to save your time, here is the updated code, with a little correction to the loop:

```python
import pyttsx3, PyPDF2

title = input("Which book would you like to listen to?\n") + ".pdf"
pdfreader = PyPDF2.PdfReader(open(title, 'rb'))
speaker = pyttsx3.init()

first_page = input("Starting with what page?\n")
last_page = input("Ending with what page?\n")

text = ""

for page_number in range(int(first_page - 1), int(last_page)):
      text = text + pdfreader.pages[page_number].extract_text()

clean_text = text.strip().replace('\n', ' ')
print(clean_text)

speaker.save_to_file(clean_text, 'result2.mp3')
speaker.runAndWait

speaker.stop()
```

Now this version correctly prints out the converted text, but fails to create the mp3 file, don't know why. Chat GPT created this version of the code, which works, and the resulting voice reading is actually surprisingly clear:

```python
import fitz  # PyMuPDF
import pyttsx3

#Get the input file name
title = input("Which book would you like to listen to?\n") + ".pdf"

#Initialize the text-to-speech engine
speaker = pyttsx3.init()

#User input for page range
first_page = int(input("Starting with what page?\n"))
last_page = int(input("Ending with what page?\n"))

#Initialize an empty text variable
text = ""

#Open the PDF file
pdf_document = fitz.open(title)

#Loop through pages and extract text
for page_number in range(first_page - 1, min(last_page, len(pdf_document))):
    page = pdf_document.load_page(page_number)
    text += page.get_text()

#Close the PDF document
pdf_document.close()

#Save the MP3 file
mp3_output = input("How would you like to call the resulting .mp3 file?\n") + ".mp3"
speaker.save_to_file(text, mp3_output)
speaker.runAndWait()
speaker.stop()

print(f"Text extracted and saved as {mp3_output}")
```