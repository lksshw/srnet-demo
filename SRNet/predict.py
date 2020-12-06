import tensorflow as tf
from SRNet.model import SRNet
import numpy as np
import os
import SRNet.cfg as cfg
from SRNet.utils import *
from SRNet.render_text import make_standard_text as mst
import pygame
from pygame import freetype
import streamlit as st
# define model
font = '/home/niwhskal/GP1-Srnet/CRAFT-pytorch/SRNet/arial.ttf'
freetype.init()

@st.cache(allow_output_mutation=True)
def get_model():
	model = SRNet(shape = cfg.data_shape, name = 'predict')
	return model

def pred(inp, text):	
	print(inp.shape)
	tar = mst(font, text, inp.shape[:2])
	model = get_model()
	with model.graph.as_default():
		with tf.Session() as sess:
		    saver = tf.train.Saver(tf.global_variables())
		    
		    # load pretrained weights
		    saver.restore(sess, '/home/niwhskal/GP1-Srnet/CRAFT-pytorch/SRNet/model_logs/checkpoints/final')
		    # predict
		    i_s = inp 
		    i_t = tar 
		    o_sk, o_t, o_b, o_f = model.predict(sess, i_t, i_s)
		    return o_f, tar
			