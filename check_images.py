#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Siquiqui Gomani
# DATE CREATED:  26/10/2019                                
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
import argparse
from time import time, sleep
from os import listdir

# Imports classifier function for using CNN to classify images
from classifier import classifier

# Imports print functions that check the lab
from print_functions_for_lab_checks import *   

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # TODO 0: Measures total program runtime by collecting start time
    start_time = time()
    
    # creates and retrieves command Line Arguments
    in_arg = get_input_args()
    # Function that checks command line arguments using in_arg
    check_command_line_arguments(in_arg)
    # Creates pet image labels by creating a dictionary
    answers_dic = get_pet_labels(in_arg.dir)
    
    check_creating_pet_image_labels(answers_dic)
    # Creates classifier labels with classifier function, compares labbels and createsa results 
    # dictionary
    result_dic = classify_images(in_arg.dir, answers_dic, in_arg.arch)
    # Function that checks results dictionary result_dic
    check_classifying_images(result_dic)
    # Adjusts the results dictionary to determine if classifier correctly classified 
    # images 'a dog'
    # or 'not a dog'
    adjust_results4_isadog(result_dic, in_arg.dogfile)
    # Function that checks results dictionary for is-a -dog adjustment - result-dic
    check_classifying_labels_as_dogs(result_dic)
    # Calculates results of run and puts statistics in results_stats_dic
    results_stats_dic = calculates_results_stats(result_dic)
    # Function that checks results stats dictionary - results_stats_dic
    check_calculating_results(result_dic,results_stats_dic)
    # Prints Summary results, incorrect classifications of dogs and breeds if requested
    print_results(result_dic, results_stats_dic, in_arg.arch, True, True )
    # Measure total program runtime by collecting end time
    end_time = time()
    # Computes overall runtime in seconds and prints it hh:mm:ss format
    tot_time = end_time - start_time
    print('\n** Total elapsed runtime:', str(int((tot_time / 3600)))
          + ':' + str(int((tot_time % 3600) / 60))
          + ':' +str(int((tot_time % 3600) % 60)))
   
    # TODO 1: Define get_input_args function within the file get_input_args.py
    
    # TODO 2: Define get_pet_labels function within the file get_pet_labels.py

                
    # Once the get_pet_labels function has been defined replace 'None' 
    # in the function call with in_arg.dir  Once you have done the replacements
    # your function call should look like this: 
    #             get_pet_labels(in_arg.dir)
    # This function creates the results dictionary that contains the results, 
    # this dictionary is returned from the function call as the variable results
    

    # Function that checks Pet Images in the results Dictionary using results    
    
    # TODO 3: Define classify_images function within the file classiy_images.py

    # TODO 0: Measure total program runtime by collecting end time
    # end_time = time()
    
    # TODO 0: Computes overall runtime in seconds & prints it in hh:mm:ss format
    

# Call to main function to run the program
if __name__ == "__main__":
    main()