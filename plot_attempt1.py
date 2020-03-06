import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nylon = pd.read_csv('/mnt/c/Users/seans/Downloads/20191120 Set2Sample5b-1%.csv')

nylon

nylon.plot.scatter('x', 'y')

