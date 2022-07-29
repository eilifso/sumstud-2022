import dispatch.yt
import numpy as np
import matplotlib.pyplot as plt

# gamma in gas law
gamma = 1.4

#Get axis from user
axis=input("Enter axis (x, y or z)")
if axis=='x':
	int_axis=0
if axis=='y':
	int_axis=1
if axis=='z':
	int_axis=2

# load data from Dispatch
run = 'sod_bifrost_'+axis
#run outside the python directory inside the experiment
data='data/'

ds=dispatch.yt.snapshot(20, run=run, data=data)


# load ray on axis
ray = ds.ortho_ray(int_axis,(0,0))
ray_sort = np.argsort(ray[axis])

# Dispatch quantities
x = np.array(ray[axis][ray_sort])

rho = np.array(ray['gas','density'][ray_sort])
u_x = np.array(ray['gas','velocity_'+axis][ray_sort])
ee = np.array(ray['stream','ee'][ray_sort])
# equation of state
p = rho*(gamma - 1)*ee

#plot density
plt.figure(1)
plt.plot(x, rho, label='stagger2/bifrost', color='r')
plt.xlabel(axis)
plt.ylabel(r'$\rho$')
plt.legend()
plt.savefig(run+'_rho_yt.png')

#plot pressure
plt.figure(2)
plt.plot(x, p, label='stagger2/bifrost', color='r')
plt.xlabel(axis)
plt.ylabel(r'$p$')
plt.legend()
plt.savefig(run+'_p_yt.png')
