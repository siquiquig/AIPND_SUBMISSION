#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Siquiqui Gomani
# DATE CREATED: 26/10/2019                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# Extracts filenames from folder pet_images
filename_list = listdir('pet_images/')
# Prints filenames from pet_images folder
print('n\Prints all filenames from pet_images/')
for idx in range(0,10,1):
    print('%2d file: %-25s'  % (idx + 1,filename_list[idx]))

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    # creates list of files in directory 
    in_files = listdir(image_dir)
    # processes each of the files to create a dictionarywhere the key is the filename and value is the 
    # picture label
    # Creates empty dictionary for the labels
    petlabels_dic = dict()
    # processes through each file in the directory, extracting only the words of the file that contains
    # the pet image label
    for idx in range(0,len(in_files),1):
        if in_files[idx][0] != '.':
        # uses split to extract words of filename into list image_name
           image_name = in_files[idx].split('_')
        # creates temporary label variable to hold pet label name extracted 
           pet_label = ' '
           for word in image_name:
               if word.isalpha():
                  pet_label += word.lower() + ' '
    #strips off trailing white space
           pet_label = pet_label.strip()
           if in_files[idx] not in petlabels_dic:
              petlabels_dic[in_files[idx]] = pet_label
           else:
                print('Warning: Duplicate file exist in directory', in_files[idx])
    # returns dictionary of labels 
    return(petlabels_dic)               
