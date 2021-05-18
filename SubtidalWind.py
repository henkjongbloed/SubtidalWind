import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
from SModelfun import SingleNonDim
from matplotlib import ticker, cm
from PSweepfun import ParameterSweep
from GeneralModelFun import plotModel, plotSpace, symlog10, invsymlog10, plotDim, plotNDim, globalParameters, plot3D, Ralston, Sverdrup, makeDicts, makeNDDict, plotSModel
import matplotlib.colors as co
from scipy.interpolate import griddata
from matplotlib.animation import FuncAnimation
import time
import warnings
import sys


np.seterr(divide = 'ignore') 
warnings.filterwarnings('ignore')
plt.rcParams['axes.xmargin'] = 0
gp = globalParameters(R = 2) #Setting parameters such as BC, alpha


dd, ndd = makeDicts(gp, 'H', tau_w=0.015)
PS = ParameterSweep(gp,ndd,1).run()
plotDim(PS, dd)
# Hello World!

dd, ndd = makeDicts(gp, 'Q', 'H', tau_w = .01)
PS = ParameterSweep(gp,ndd,1).run()
plotDim(PS, dd)
# Hello World!

ndd = makeNDDict(gp)
SM = SingleNonDim(gp, ndd).run()
plotSModel(SM)
#ndd2 = makeNDDict(gp)
plt.show()

'''
expar = ['']
EX, dd = [], 10*[None]
for ex in range(10):
    dd[ex], ndd = makeDict(gp, 'H', Q = (ex**2+1)*10, tau_w = .02)
    EX.append(ParameterSweep(gp, ndd, 1))

EXr = [ex.run() for ex in EX]
[plotSmodel(exr, ddr) for exr,ddr in zip(EXr,dd)]

expar = ['']
EX,dd = [], 10*[None]
for ex in range(10):
    dd[ex], ndd = makeDict(gp, 'H', Q = (ex**2+1)*10, tau_w = .02)
    EX.append(ParameterSweep(gp, ndd, 1))

EXr = [ex.run() for ex in EX]
[plotDim(exr, ddr, 'H') for exr,ddr in zip(EXr,dd)]

#PS3.run()
'''
#plt.show()