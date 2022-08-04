# Overplot einfeldt in x, y and z

# timestep = 10
timestep = int(input('plot which snapshot? (0-20) >> '))

import dispatch.yt
import numpy as np
import matplotlib.pyplot as plt

# Gamma in gas law
gamma = 1.4

# Load data from Dispatch
runs = ['einfeldt_x', 'einfeldt_y', 'einfeldt_z']
# Run outside the python directory inside the experimenti
data='data/'

axes = ['x', 'y', 'z']

# Create empty lists for all variables
ds, rays, ray_sorts, x, rho, u, ee, p, internal = ([] for i in range(9))

# Loop over x, y, and z axes
for i, axis in enumerate(axes):

	ds.append( dispatch.yt.snapshot(timestep, run=runs[i], data=data) )

	# Load ray on axis
	rays.append( ds[i].ortho_ray(i,(0,0)) )
	ray_sorts.append( np.argsort(rays[i][axis]) )

	# Dispatch quantities	
	x.append( np.array(rays[i][axis][ray_sorts[i]]) )
	rho.append( np.array(rays[i]['gas', 'density'][ray_sorts[i]]) )
	u.append( np.array(rays[i]['gas', 'velocity_' + axis][ray_sorts[i]]) )
	ee.append( np.array(rays[i]['stream', 'ee'][ray_sorts[i]]) )
	p.append( rho[i]*(gamma-1)*ee[i] )
	internal.append( p[i]/rho[i]/(gamma-1) )


lines = ['-.', '--', ':']

# Subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
for i, axis in enumerate(axes):

	# Density	
	ax1.plot(x[i], rho[i], lines[i], label=axis)
	ax1.legend(); ax1.grid()
	ax1.set_ylabel(r'$\rho$')

	# Pressure
	ax2.plot(x[i], p[i], lines[i], label=axis)
	ax2.set_ylabel(r'$P$')
	ax2.legend(); ax2.grid()

	# Velocity
	ax3.plot(x[i], u[i], lines[i], label=axis)
	ax3.set_ylabel(r'$u$')
	ax3.legend(); ax3.grid()

	# Specific internal energy
	ax4.plot(x[i], internal[i], lines[i], label=axis)
	ax4.set_ylabel(r'$P/\rho$')
	ax4.legend(); ax4.grid()

fig.suptitle(f'Snapshot {timestep}')
plt.tight_layout()
plt.savefig(f'einfeldt_subplot_{timestep}.png')
plt.show()

