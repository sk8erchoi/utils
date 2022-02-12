import glob
import win32com.client as win32
import os

word = win32.Dispatch('Word.Application')
word.Visible = True

for f in glob.iglob(r'**\*.docx', recursive=True):
    p = os.getcwd() + os.sep + f
    print(f'Opening {p}...')
    word.Documents.Open(p)
