import random
from PIL import Image
import os
import tkinter.filedialog as fd



# function for generating random image from random seed value
def generate_image(seed):
    width = 512
    height = 256
    
    color_range = range(int(255))
    image = Image.new('RGB', (width, height), 'white')
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            rn = random.randint(0, 100)
            rc = random.randint(1, 3)

            if rn < 30:
                
                if   rc == 1:
                    pixels[x,y] = (255, 0, 0)
                elif rc == 2:
                    pixels[x,y] = (0, 255, 0)
                elif rc == 3:
                    pixels[x,y] = (0, 0, 255)                        
            elif rn < 50:
                n = random.choice(color_range)
                pixels[x,y] = (n, n, n)                    
            else:
                pixels[x,y] = (255, 255, 255)
    return image

# function generating images and saving them to output folder   
def generate_images(output_folder):
    for i in range(25):
        seed = random.choice(range(1, 999))
        # calling function to generate image
        image = generate_image(seed)  
        # generate name for image
        data_number = str(i).zfill(3)
        filename = f'data_{data_number}.png'
        # saving the image
        image.save(os.path.join(output_folder, filename))
        seed += 1

print("Please select folder to generate images into....")
#pops the window to find path
path = fd.askdirectory()

generate_images(path)
print("Data downloaded")



    








