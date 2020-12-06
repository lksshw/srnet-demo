import os
import numpy as np 
import streamlit as st
import imgproc
import cv2
checkpoints_dir = '/home/niwhskal/GP1-Srnet/CRAFT-pytorch/checkpoint_app/'

class GUI():

    def __init__(self):
        
        self.params = {}
        self.draw()

        self.Craft_ckpt = '/home/niwhskal/GP1-Srnet/CRAFT-pytorch/checkpoint_app/craft_mlt_25k.pth'

    def draw(self):
       
        st.write('# SRNET Demo')
        st.write('A basic application to demonstrate the utility of SRNet')
        st.write('Please make sure that the pretrained weights for SRNet are placed in the appropriate folder while running')
        self.img_choice = st.sidebar.radio("Select a method of input", ('Image URL', 'DEMO Images', 'Upload Image')) 


    def get_img(self):

        if self.img_choice == 'DEMO Images':
            self.demo_image_examples = {"Poster1": "/home/niwhskal/GP1-Srnet/CRAFT-pytorch/figures/popster1.jpg",
                                    "Poster2": "/home/niwhskal/GP1-Srnet/CRAFT-pytorch/figures/poster2.jpg",
                                    "Poster3": "/home/niwhskal/GP1-Srnet/CRAFT-pytorch/figures/poster3.jpg",
                                    "Poster4": "/home/niwhskal/GP1-Srnet/CRAFT-pytorch/figures/poster4.jpg",
                                    "Poster5": "/home/niwhskal/GP1-Srnet/CRAFT-pytorch/figures/poster5.jpg",
                                    "Poster6": "/home/niwhskal/GP1-Srnet/CRAFT-pytorch/figures/poster6.jpg",
                                    "Poster7": "/home/niwhskal/GP1-Srnet/CRAFT-pytorch/figures/poster7.jpg",
                                    "Poster8": "/home/niwhskal/GP1-Srnet/CRAFT-pytorch/figures/poster8.jpg",
                                    "Poster9": "/home/niwhskal/GP1-Srnet/CRAFT-pytorch/figures/poster9.jpg"}



                                    
 
            self.ch_path = st.selectbox('Select an image from list', list(self.demo_image_examples.keys()))
            self.img_path = self.demo_image_examples[self.ch_path] 

            def load_img(img_path):
                image = imgproc.loadImage(img_path)
                image = cv2.resize(image, (300,500))
                return image
            
            self.img = load_img(self.img_path)

        return self.img