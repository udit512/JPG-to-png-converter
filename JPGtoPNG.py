import sys
import os
from PIL import Image


#grab the arguments 
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if the output folder exists
if os.path.exists(output_folder) == False:
	os.makedirs(output_folder)

#loop through the directory
for filename in os.listdir(image_folder):
	if filename.endswith(".jpg"):
		img = Image.open(image_folder+"/"+filename)
		clean_name = os.path.splitext(filename)[0]
		#print(clean_name)
		img.save(output_folder+"/"+clean_name+".png","png")