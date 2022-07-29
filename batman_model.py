import batman
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib import rc

params = batman.TransitParams()
params.t0 = 0. 				#time of inferior conjunction
params.per = 1.				#orbital period
params.rp = 0.1				#planet radius (in units of stellar radii)
params.a = 15.				#semi-major axis (in units of stellar radii)
params.inc = 87.			#orbital inclination (in degrees)
params.ecc = 0.				#eccentricity
params.w = 90.				#longitude of periastron (in degrees)
params.u = [0.1, 0.3] 	      	        #limb darkening coefficients
params.limb_dark = "quadratic"          #limb darkening model

t = np.linspace(-0.025, 0.025, 1000)    	#times at which to calculate light curve
m = batman.TransitModel(params, t)	        #initializes model
flux = m.light_curve(params)

data = [t, flux]
np.savetxt("results", data)


plt.plot(np.loadtxt("results")[0], np.loadtxt("results")[1])
plt.xlabel("Time from central transit (days)")
plt.ylabel("Relative flux")
plt.ylim((0.989, 1.001))
plt.show()
