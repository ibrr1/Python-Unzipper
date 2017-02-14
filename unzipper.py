import os, zipfile

dir_name = '/Users/ibrahim/Desktop/scrapy-tut/Apps'
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

text_file = open("Failed_files.txt", "w")


for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files

    try:
        print "Unzipping", item
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file
        print "Success"
        print "========================================"
    except:
        print "Failed to unzip ", item
        text_file.write(item+ "\n")
        print "========================================"
        pass

text_file.close()


