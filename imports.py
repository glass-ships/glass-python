###########################################
#   Setup standard analysis environment   # 
###########################################

import os, sys
from math import *

import pandas
import numpy as np
#np.set_printoptions(threshold=np.inf)

import scipy
import scipy.integrate as spi
from scipy import stats

# Plotting modules
import matplotlib.pyplot as plt
from matplotlib import style
#import matplotlib.image as mpimg
%matplotlib inline
style.use('ggplot')

from bokeh.plotting import figure, output_notebook, show
output_notebook(hide_banner=True)

# LaTeX rendering in plots 
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)