import numpy as np
import matplotlib.pyplot as plt
# %matplotlib agg
import pandas as pd
import os
import preprocessing as pp


def test_graph_and_save():
    source = os.getcwd()
    big_folder = os.path.dirname(source) + '/Raman_Data'
    with os.scandir(big_folder) as entries:
        for entry in entries:
            foldername = entry.name
            print(foldername)
            with os.scandir(big_folder + '/' + foldername) as entries:
                for entry in entries:
                    filename = entry.name
    data = pd.read_csv(big_folder + '/' + foldername + '/' + filename , sep='\s+')
    name = filename + "_" + foldername + ".png"
    pp.graph_and_save(data, name)
    assert len(data) is not 2, 'the dataframe needs to have two columns'
    assert isinstance(data, pd.DataFrame) == True, 'you need to put a Dataframe inside'
    
def test_preprocessing():
    source = os.getcwd()
    big_folder = os.path.dirname(source) + '/Raman_Data'
    pp.preprocessing(big_folder)
    with os.scandir(big_folder) as entries:
        for entry in entries:
            foldername = entry.name
            pnumber = 0
            if foldername.endswith(".txt"):
                pnumber = pnumber + 1
    assert pnumber is not 0,'There is no txt file in the' + big_folder