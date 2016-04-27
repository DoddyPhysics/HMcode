import matplotlib.pyplot as pl
import matplotlib as mpl
import numpy as np
import math

meadpower=np.loadtxt('power.dat',unpack=True)
# The frist row of spectrum is ###, and labels the redshift columns
# numpy does not read this, it is taken as a comment
# First column is k's, subsequent columns are \Delta^2(k) at redshifts
meadshape=np.shape(meadpower)
num_reds=meadshape[0]-1
num_ks=meadshape[1]

kmead=meadpower[0,:]



for i in range(1,num_reds+1):
	d2=meadpower[i,:]
	pkmead=d2/kmead**3./(2.*math.pi**2.)
	pl.plot(kmead,pkmead)
pl.xscale('log')
pl.xlim([kmead.min(),kmead.max()])
pl.yscale('log')
pl.show()