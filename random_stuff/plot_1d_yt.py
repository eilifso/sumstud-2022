import dispatch.yt
import numpy as np
import matplotlib.pyplot as plt

# gamma in gas law
gamma = 1.4

# load data from Dispatch
run = 'brio-wu_bifrost_y'
#run outside the python directory inside the experiment
data='data/'

ds=dispatch.yt.snapshot(10, run=run, data=data)

# load ray on x-axis
ray = ds.ortho_ray(1,(0,0))
ray_sort = np.argsort(ray["y"])

# Dispatch quantities
y = np.array(ray['y'][ray_sort])
rho = np.array(ray['gas','density'][ray_sort])
u_y = np.array(ray['gas','velocity_y'][ray_sort])
ee = np.array(ray['stream','ee'][ray_sort])
# equation of state
p = rho*(gamma - 1)*ee

#plot density
plt.figure(1)
plt.plot(y, rho, 'y', label='stagger2/bifrost', color='r')
plt.xlabel('y')
plt.ylabel(r'$\rho$')
plt.legend()
plt.savefig(run+'_rho.png')

#plot pressure
plt.figure(2)
plt.plot(y, p, 'y', label='stagger2/bifrost', color='r')
plt.xlabel('y')
plt.ylabel(r'$p$')
plt.legend()
plt.savefig(run+'_p.png')

