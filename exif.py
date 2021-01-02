from PIL import Image
import bcolors
import sys, argparse
import os


def banner():
    print("""
                ███████╗██╗░░██╗██╗███████╗░░░░░░███████╗██╗░░██╗████████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
                ██╔════╝╚██╗██╔╝██║██╔════╝░░░░░░██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
                █████╗░░░╚███╔╝░██║█████╗░░█████╗█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
                ██╔══╝░░░██╔██╗░██║██╔══╝░░╚════╝██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
                ███████╗██╔╝╚██╗██║██║░░░░░░░░░░░███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
                ╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                                                                                                 Coded By - NG  """
                 )

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] != 'i'):
       try:
        input_image = sys.argv[2]
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", required=True)
# File
        if  '.txt' in input_image:
            if (os.path.exists(input_image) == True):
               file = open(input_image, "r")
               lines = file.readlines()
               for te in lines:
                   r= te.replace('\'', '')
                   Strip_input_image = r.strip()
                   print(bcolors.BOLD, 'Image properties for image:', Strip_input_image, '\n''\n')
                   print(bcolors.OKMSG + "--------------------------File------------------------------")
                   try:
                        print(bcolors.BOLD + "Image Name: ", os.path.split(Strip_input_image)[1])
                   except:
                        print(bcolors.ERRMSG + "File properties for this particular image Not exists")

                   print(bcolors.OKMSG + "-------------------------Image Dimensions-------------------")
                   try:
                        print(bcolors.BOLD + "Height: ", Image.open(Strip_input_image).getexif()[40962])
                        print(bcolors.BOLD + "Width: ", Image.open(Strip_input_image).getexif()[40963])
                        print(bcolors.BOLD + "Dimensions: ", Image.open(Strip_input_image).getexif()[40963], '*', Image.open(Strip_input_image).getexif()[40962])
                   except:
                        print(bcolors.ERRMSG + "Image Dimensions properties for this particular image Not exists")
# Camera
                   print(bcolors.OKMSG + "-------------------------Camera Details--------------------")
                   try:
                        print(bcolors.BOLD + "Maker: ", Image.open(Strip_input_image).getexif()[271])
                        print(bcolors.BOLD + "Model:", Image.open(Strip_input_image).getexif()[272])
                        print(bcolors.BOLD + "Expousre time: ", Image.open(Strip_input_image).getexif()[33434], 'in sec')
                        print(bcolors.BOLD + "F-stop: ", 'f/', Image.open(Strip_input_image).getexif()[33437])
                   except:
                        print(bcolors.ERRMSG + "Camera properties for this particular image Not exists")
# Origion
                   print(bcolors.OKMSG + "-------------------------Origions Details------------------")
                   try:

                        print(bcolors.BOLD + "Authors: ", Image.open(Strip_input_image).getexif()[315])
                        print(bcolors.BOLD + "Date Taken: ", Image.open(Strip_input_image).getexif()[306])
                        print(bcolors.BOLD + "Copyrights: ", Image.open(Strip_input_image).getexif()[33432])
                   except:
                        print(bcolors.ERRMSG + "Origion properties for this particular image Not exists")
# Advanced
                   try:
                        print(bcolors.OKMSG + "****Advanced****")
                        print(bcolors.BOLD + "Exif Version: ", Image.open(Strip_input_image).getexif()[36864])
                   except:
                        print(bcolors.ERRMSG + "Advanced properties for this particular image Not exists")
        else:
# File
               print(bcolors.OKMSG + "---------------------------File------------------------------")
               try:
                   print(bcolors.BOLD + "Image Name: ", os.path.split(input_image)[1])
               except:
                   print(bcolors.ERRMSG + "File properties for this particular image Not exists")

# image dimensions
               print(bcolors.OKMSG + "----------------------Image Dimensions-------------------------")
               try:
                   print(bcolors.BOLD + "Height: ", Image.open(input_image).getexif()[40962])
                   print(bcolors.BOLD + "Width: ", Image.open(input_image).getexif()[40963])
                   print(bcolors.BOLD + "Dimensions: ", Image.open(input_image).getexif()[40963], '*', Image.open(input_image).getexif()[40962])
               except:
                   print(bcolors.ERRMSG + "Image Dimensions properties for this particular image Not exists")
# Camera
               print(bcolors.OKMSG + "---------------------Camera Details--------------------------")
               try:
                   print(bcolors.BOLD + "Maker: ", Image.open(input_image).getexif()[271])
                   print(bcolors.BOLD + "Model:", Image.open(input_image).getexif()[272])
                   print(bcolors.BOLD + "Expousre time: ", Image.open(input_image).getexif()[33434], 'in sec')
                   print(bcolors.BOLD + "F-stop: ", 'f/', Image.open(input_image).getexif()[33437])
               except:
                   print(bcolors.ERRMSG + "Camera properties for this particular image Not exists")
# Origion
               try:
                   print(bcolors.OKMSG + "-----------------------Origions Details--------------------------")
                   print(bcolors.BOLD + "Authors: ", Image.open(input_image).getexif()[315])
                   print(bcolors.BOLD + "Date Taken: ", Image.open(input_image).getexif()[306])
                   print(bcolors.BOLD + "Copyrights: ", Image.open(input_image).getexif()[33432])
               except:
                   print(bcolors.ERRMSG + "Origion properties for this particular image Not exists")
# Advanced
               try:
                   print(bcolors.OKMSG + "***********************Advanced*****************************")
                   print(bcolors.BOLD + "Exif Version: ", Image.open(input_image).getexif()[36864])
               except:
                   print(bcolors.ERRMSG + "Advanced properties for this particular image Not exists")

       except:
            print(bcolors.OKMSG + 'Please enter python exif.py -i <valid image location > ')
elif (sys.argv[1] == '-h'):
    print(bcolors.BOLD + 'usage: exif.py [-h] -i IMAGE' '\n' 'OPTIONS:' '\n' '-h,--help    '
                         'show this help message and exit' '\n''-i IMAGE,   --iamge Loaction of image which exif properties you want to check')
elif (sys.argv[1] != '-i'):
    print(bcolors.OKMSG + 'Please enter -i < valid image location  >')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -i or -h, with a valid image location ')

