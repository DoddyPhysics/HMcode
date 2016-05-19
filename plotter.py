import matplotlib.pyplot as pl
import matplotlib as mpl
import numpy as np
import math

power1=np.loadtxt('mw1_conc_barrier.dat',unpack=True)
power2=np.loadtxt('mw1_conc_barrier_test.dat',unpack=True)

# The frist row of spectrum is ###, and labels the redshift columns
# numpy does not read this, it is taken as a comment
# First column is k's, subsequent columns are \Delta^2(k) at redshifts
meadshape=np.shape(power1)
num_reds=meadshape[0]-1
num_ks=meadshape[1]

k1=power1[0,:]
k2=power1[0,:]



for i in range(1,num_reds+1):
	d1=power1[i,:]
	d2=power2[i,:]
	#pkmead=d/kmead**3./(2.*math.pi**2.)
	pl.plot(k1,d1,'-')
	pl.plot(k2,d2,'--')
pl.xscale('log')
pl.xlim([k1.min(),k1.max()])
pl.yscale('log')
pl.show()


for i in range(1,num_reds+1):
	d1=power1[i,:]
	d2=power2[i,:]
	#pkmead=d/kmead**3./(2.*math.pi**2.)
	pl.plot(k1,(d1-d2)/d1,'-')
pl.xscale('log')
pl.xlim([k1.min(),k1.max()])
pl.yscale('linear')
pl.show()