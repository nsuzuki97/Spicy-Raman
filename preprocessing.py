import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib agg
import pandas as pd
import os


def graph_and_save (source, data, name):
    y = data.iloc[:, 1]
    x = data.iloc[:, 0]
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(x, y, label='$y = numbers')
    ax.legend()
    fig.savefig(source + '/Pre_Augmented_Raman_Pictures/' + name)
    #print(type(fig))
    plt.close('all')
    
    
def preprocessing(source, big_folder):
    os.listdir()
    with os.scandir(big_folder) as entries:
        for entry in entries:
            foldername = entry.name
            print(foldername)
            with os.scandir(big_folder + '/' + foldername) as entries:
                for entry in entries:
                    filename = entry.name
                    data = pd.read_csv(big_folder + '/' + foldername + '/' + filename , sep='\s+')
                    name = filename + "_" + foldername + ".png"
                    graph_and_save(source, data, name)
