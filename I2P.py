from PIL import Image
import os
import sys
import tkinter
from tkinter import filedialog
import time

def fileselect():
    root = tkinter.Tk()
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir,title='Please select an Image file')
    root.destroy()
    if len(tempdir) > 0:
        return (tempdir)
        
def folderselect():
    '''from PIL import Image
    import tkinter
    from tkinter import filedialog
    import os'''
    root = tkinter.Tk()
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    root.destroy()
    if len(tempdir) > 0:
        return (tempdir)
    else:
        print("Folder not selected")
        return folderselect()
        
def MainConverter():    
    print("Let's convert a file\n")
    time.sleep(1)
    file=fileselect()
    print("You selected : %s"%file)
    image1 = Image.open(r'%s'%file)
    im1 = image1.convert('RGB')
    print("Now let's select a folder for the PDF file\n")
    time.sleep(1.5)
    folder=folderselect()
    time.sleep(1)
    print("You selected : %s"%folder)
    pdf_name=input("Enter pdf file name without the '.pdf' :\n")
    if pdf_name=="":
        pdf_name="I2P"
    pdf_path=folder+"/"+pdf_name+".pdf"
    im1.save(r'%s'%pdf_path)
    print("\nSuccessfully converted and saved!")

def Repeater():
    option=int(input("Press '0/y/Y' to exit or '1/n/N' to download another track: \n"))
    if option in [1,"n","N"]:
        Doer()
    elif option in [0,"y","Y"]:
        sys.exit()
    else:
        option=int(input("Incorrect input entered, try again! :"))

def Doer():
    MainConverter()
    Repeater()

if __name__ == "__main__":
    Doer()
