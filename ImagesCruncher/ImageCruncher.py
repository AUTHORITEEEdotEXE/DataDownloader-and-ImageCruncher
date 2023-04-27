import os
from PIL import Image
import json
import tkinter.filedialog as fd


# function to count pixels of images in the folder
def count_pixels(folder_path):
     # create an empty dictionary to store the results
     results = {}
     # cyklus: folder
     for filename in os.listdir(folder_path):
         if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith("jpeg") or filename.endswith(".webp"): # filter what to read
             filepath = os.path.join(folder_path, filename)
             # open images
             with Image.open(filepath) as img:
                
                 pixels = list(img.getdata())
                 # counters at 0 
                 red_pixels = 0
                 green_pixels = 0
                 blue_pixels = 0
                 other_pixels = 0
                 # cycle: colors
                 for pixel in pixels:
                     if pixel[0] == 255 and pixel[1] == 0 and pixel[2] == 0: 
                         red_pixels += 1
                     elif pixel[1] == 255 and pixel[0] == 0 and pixel[2] == 0: 
                         green_pixels += 1
                     elif pixel[2] == 255 and pixel[0] ==0 and pixel[1] == 0: 
                         blue_pixels += 1
                     else:
                         other_pixels += 1
                 # file ID without extension
                 file_id = os.path.splitext(filename)[0]
                 # format of the table
                 results[file_id] = {"RED": red_pixels, "GREEN": green_pixels, "BLUE": blue_pixels, "OTHER": other_pixels}
     # save to the .json
     with open("ResultsJSON.json", "w") as jsonfile:
        # dump results 
        json.dump(results, jsonfile)

       
print("Please select folder to get data from...") 
#pops the window to find path   
path = fd.askdirectory()
# calling function 
count_pixels(path)
print("Data saved in ResultsJSON.json")
