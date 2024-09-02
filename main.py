import pyttsx3
import PyPDF2
import os

# input_filepath = 'c:\Users\Huw Rees\code\personal\tutorials\TiffInTech\pdf2mp3\' 
filename = 'CV_Huw_Rees'
input_path = 'tutorials\\TiffInTech\\pdf2mp3\\'
input_pdf = input_path + filename + '.pdf'

print(input_pdf)
# output_mp3 = 'tutorials\TiffInTech\pdf2mp3\test.mp3'
output_mp3 = 'test.mp3'

pdfreader = PyPDF2.PdfReader(open(input_pdf, 'rb'))

# print(len(pdfreader.pages))
# print(pdfreader.pages)

for page_num in range(len(pdfreader.pages)):
    print(page_num)

print(range(len(pdfreader.pages)))

full_text = ''

for page_num in range(len(pdfreader.pages)):
    # page = pdfreader.pages[page_num]
    # print(page.extract_text())
    text = pdfreader.pages[page_num].extract_text()
    
    clean_text = text.strip().replace('\n', ' ')
    # print(clean_text)

    if page_num > 0:
        full_text += 'NEW PAGE' + clean_text
    else:
        full_text = clean_text

print(full_text)


# "Saving Voice to a file"
# On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine = pyttsx3.init()
# engine.say("Saving pdf contents to mp3 file")
# engine.runAndWait()
# engine.stop()

engine = pyttsx3.init()

try:
    engine.save_to_file(full_text, 'text.mp3')
    engine.runAndWait()
except:
    print('Text was not saved to mp3 file')

engine.stop()


# Source file path
source = 'text.mp3'
# destination file path
dest = f'./tutorials/TiffInTech/pdf2mp3/{filename}.mp3' 

# try renaming the source path
# to destination path
# using os.rename() method
try :
    os.rename(source, dest)
    print("Source path renamed to destination path successfully.")
# If Source is a file 
# but destination is a directory
except IsADirectoryError:
    print("Source is a file but destination is a directory.")
# If source is a directory
# but destination is a file
except NotADirectoryError:
    print("Source is a directory but destination is a file.")
# For permission related errors
except PermissionError:
    print("Operation not permitted.")
# For other errors
except OSError as error:
    print(error)

