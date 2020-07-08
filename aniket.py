# Firstly we have to import os module ,it is quite obvious why
# we need to import os module.os stands for operating system ,as we working with os
# so we need to import it 
import os
# This method will create folder you just need to pass the folder name in this
#  method this will create folder in your working directory.Remember it will not create the folder
# with name which is already present in the directory
def createFolderIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
#This method will move your all files to the destination folder ,you just need to 
# pass the folder name and collection of files with same extension
def MoveFileToTheirRespectiveFolder(foldername,folderfiles):
    for file in folderfiles:
        os.replace(file,f"{foldername}/{file}")
#Main method starting of the program
if __name__=="__main__":
    # os.listdir() it will list all your files or folders and stor it in files[] 
    files=os.listdir()
    # this method is to remove a particular file
    files.remove('aniket.py')
    #print(files)
    #Calling the function to create folder
    createFolderIfNotExists('Images')
    createFolderIfNotExists('Html')
    createFolderIfNotExists('Other')
    #Create a list to classify images on the basis of extension
    imageExt=[".jpg",".jpeg",".png"]
    #using list comprehension to create imag list for storing of all files with extension of image
    imag=[f for f in files if os.path.splitext(f)[1].lower() in imageExt]
    # Create a list to classify documents on the basis of extensions
    docExt=[".css",".txt",".html",".pdf",".ppt",".doc",".docx",".xlsm",".xls",".xlsx",".pptx"]
    #Create docs list which contains all document extension files
    docs=[f for f in files if os.path.splitext(f)[1].lower() in docExt]
    #Create others list to store all files except image and documents
    others=[]
    for f in  files:
        ext=os.path.splitext(f)[1].lower()
        if(( ext not in docExt) and (ext not in imageExt) and os.path.isfile(f) ):
            others.append(f)
    #Moving all files to their respective folder
    MoveFileToTheirRespectiveFolder("Images",imag)
    MoveFileToTheirRespectiveFolder("Html",docs)
    MoveFileToTheirRespectiveFolder("Other",others)
