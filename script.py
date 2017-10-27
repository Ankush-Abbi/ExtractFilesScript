import os
from shutil import copyfile, rmtree
folders = [name for name in os.listdir(".") if os.path.isdir(name)]		#get the list of the folder in the current location
cwd = os.getcwd()														#get the current directory path
for folderName in folders:
	location = cwd + '\\' + folderName									#creating location variable which points inside the folder 
	files = [file for file in os.listdir(location)]  					#listing files in that particular folder
	counter = 0															#initiating counter for multiple files
	for data in files:													#checking each file
		extension = os.path.splitext(data)[1]							#extracting extension of each file
		copyfile(location + '\\' + data, location + str(counter) + extension)		#copying file to the laoction outside the folder that includes it
		counter = counter + 1	
	rmtree(folderName)													#remove the folder