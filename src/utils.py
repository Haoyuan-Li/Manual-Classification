import numpy as np
from tkinter import *
from tkinter import ttk
import glob


def load_image(ind):
    pattern = PhotoImage(master=mainframe, file=image_files[0])
    Img['image'] = pattern
    
    return

def load_data(address):
    image_files = glob.glob(address+'*_data.png')
    load_image(0)
    return 

def create_label():
    pass
    return

def load_label():
    pass
    return

def save_label():
    pass
    return

def next_image():
    pass
    return

def next_run_number():
    pass
    return

def previous_image():
    pass
    return

def previous_run_number():
    pass
    return

def set_label():
    pass
    return

def test():
    # Use this test function to see whether the data and label are loaded
    if data == None:
        print('data is not loaded')
        return False
    
    if label == None:
        print('label is not loaded')
        return False
    
    return True

def test_data():
    # Use this test function to see whether the data is loaded
    if data == None:
        print('data is not loaded')
        return False
    
    return True