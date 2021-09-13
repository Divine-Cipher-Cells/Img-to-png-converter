
from PIL import Image, ImageFilter


import sys,os

current,fresh=sys.argv[1],sys.argv[2]

#  for creating png files
def makingPNG():
     with Image.open(file) as imgFile:
                imgFile.save(os.path.join(fresh,infile).replace(".jpg",".png")
                ,"png")



#  for looping through them and creating them
for infile in os.listdir(current):
    file=os.path.join(current,infile)
    if os.path.isfile(file):
        try:
            makingPNG()
        except:
            os.mkdir(fresh)
            makingPNG()
            
           
            
            
     
