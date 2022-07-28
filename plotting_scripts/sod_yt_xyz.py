import dispatch.yt
import numpy as np
import matplotlib.pyplot as plt

# Gamma in gas law
gamma = 1.4

# Load data from Dispatch
runs = ['sod_bifrost_x', 'sod_bifrost_y', 'sod_bifrost_z']
# Run outside the python directory inside the experimenti
data='data/'

axes = ['x', 'y', 'z']

# Create empty lists for all variables
ds, rays, ray_sorts, x, rho, u, ee, p = ([] for i in range(8))

# Loop over x, y, and z axes
for i, axis in enumerate(axes):

	ds.append( dispatch.yt.snapshot(20, run=runs[i], data=data) )

	# Load ray on axis
	rays.append( ds[i].ortho_ray(i,(0,0)) )
	ray_sorts.append( np.argsort(rays[i][axis]) )

	# Dispatch quantities	
	x.append( np.array(rays[i][axis][ray_sorts[i]]) )
	rho.append( np.array(rays[i]['gas', 'density'][ray_sorts[i]]) )
	u.append( np.array(rays[i]['gas', 'velocity_' + axis][ray_sorts[i]]) )
	ee.append( np.array(rays[i]['stream', 'ee'][ray_sorts[i]]) )
	p.append( rho[i]*(gamma-1)*ee[i] )


lines = ['-.', '--', ':']

# Plot density
plt.figure(1)
for i, axis in enumerate(axes):
	plt.plot(x[i], rho[i], lines[i], label=r'$\rho($' + axis + ')')
plt.xlabel('x, y, z')
plt.ylabel(r'$\rho$')
plt.legend()
plt.savefig('sod_rho.png')

# Plot pressure
plt.figure(2)
for i, axis in enumerate(axes):
	plt.plot(x[i], p[i], lines[i], label=r'$p$(' + axis + ')')
plt.xlabel('x, y, z')
plt.ylabel(r'$p$')
plt.legend()
plt.savefig('sod_p.png')

# Plot velocity
plt.figure(3)
for i, axis in enumerate(axes):
	plt.plot(x[i], u[i], lines[i], label=r'$u$(' + axis + ')')
plt.xlabel('x, y, z')
plt.ylabel(r'$u$')
plt.legend()
plt.savefig('sod_u.png')
