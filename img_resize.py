# Used to resize all images in list of directories
# Input:   Source and Destination folders. Source Folders should contain 
#          list of images to be resized.
# Method:  Each image in source folders is resized and put into the 
#          correspinding destination folders with the same name
# Output:  Destination folders contain resized images

# Things to Note:
# 1) Destination directories must be created before hand.
# 2) No exception handling done.
# 3) Source and destination folders should be actual paths and hence must 
#    contain a '/' at the end
# 4) The destination folder of a source folder is the folder in 
#    destinationFolders at the same index as the sourceFolders.

import os
from PIL import Image

sourceFolders = ['images/', '0/', '1/']
destinationFolders = ['images_resize/', '0_resize/', '1_resize/']

for i in range(len(sourceFolders)):
	sourceFolder = sourceFolders[i]
	destinationFolder = destinationFolders[i]

	files = os.listdir(sourceFolder)	

	for file in files:
		img = Image.open(sourceFolder + file)
		new_img = img.resize((96, 96))
		new_img.save(destinationFolder+file)
