# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:27:02 2018

@author: AkSangwan
"""

#------------------------------------------------------------------------------
#--------------------------------------imports---------------------------------
#------------------------------------------------------------------------------

import urllib
import os
from PIL import Image




#------------------------------------------------------------------------------
#-----------------------------------API url builder----------------------------
#------------------------------------------------------------------------------

#directory place to store
#replace or remove with the pdf stored eventually
SaveAtPath = r"C:\Users\aksangwan\StreetView" 

# method to parse and create a meaningful url out of the address
def GetStreetImage(Address,Path):   
  baseGoogleAPIAddress = "https://maps.googleapis.com/maps/api/streetview?size=1200x1200&location="
  NewUrl = baseGoogleAPIAddress + urllib.parse.quote_plus(Address) #+ key 
  fileName = Address + ".png"
  new_image = urllib.request.urlretrieve(NewUrl, os.path.join(SaveAtPath,fileName))
  return new_image



#List of addresses to get the image of
List_Addresses = ["9800 NW 41 St FL 33178"]





#------------------------------------------------------------------------------
#--------------------------------------main------------------------------------
#------------------------------------------------------------------------------
images_list=[]
for i in List_Addresses:
  image = GetStreetImage(Address=i,Path=SaveAtPath)
  images_list.append(image)
  
  
  
  
#--------------------------------------PDF--------------------------------------
img_touple =[]
for indx in range(len(images_list)):
    img_touple = images_list[indx]
    
    #name to append to default directory. Basically the name to store pdfs by
    append_name = List_Addresses[indx]
    
    #its a list of touple. So pick forst entry of each touple, which is the actual image name with .png extension
    filename = img_touple[0]
    im = Image.open(filename)
    if im.mode == "RGBA":
        im = im.convert("RGB")
    
    #get current working directory to store pdfs created    
    currentDiectory = os.getcwd()
    
    #we need name in raw string format
    currentDiectory = currentDiectory.replace("/","\\")
    
    new_fn = currentDiectory + "\\Streetview\\" + append_name +".pdf"
    
    #check if file already exists or not
    if not os.path.exists(new_fn):
        im.save(new_fn, "PDF", resolution=100.0)
    
#------------------------------------------------------------------------------
#--------------------------------------end------------------------------------
#------------------------------------------------------------------------------





