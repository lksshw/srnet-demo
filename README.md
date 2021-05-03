# SRnet-Demo

File Test.py is the main app.

You will need to download pretrained weights for:

1. The craft model: [LINK](https://drive.google.com/file/d/1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ/view?usp=drive_open) 
2. The Tensorflow SRNET model: [LINK](https://drive.google.com/drive/folders/1SJ-BAVyTxMVml5lY1r3c_LZb-XVhQl0n?usp=sharing)
3. VGG 19 tensorflow weights: [LINK](https://github.com/fchollet/deep-learning-models/releases/tag/v0.1)

Place these weights in their appropriate folders (look at the .py files for their paths)

Setup a tensorflow virtual environment (tf version 1.15)

Install all dependencies.

Run test.py in the virtual env.


Note: 
* This demo uses the tensorflow version of SRNET. Change the code to the pytorch version (on my github).
* Streamlit is extremely slow because it has to load weights for the CRAFT model as well as for the SRNET model. Find a way to change this. Feel free to build from scratch.
* You could perhaps write a script for the bounding box detection and remove the craft model.
* I won't be able to help / assist because I'm extremely busy.

Please maintain this codebase however you see fit. Once you have a fast demo running, you can opensource it through this repo. You'll get all credit of course.
