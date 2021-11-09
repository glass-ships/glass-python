###########################################
#   Setup standard analysis environment   # 
###########################################

import os, sys
from math import *

import pandas as pd
import numpy as np
#np.set_printoptions(threshold=np.inf)

import scipy
import scipy.integrate as spi
from scipy import stats

# Plotting modules
import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn-whitegrid')
%matplotlib inline

# LaTeX rendering in plots 
from matplotlib import rc
rc('text', usetex=True)
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
