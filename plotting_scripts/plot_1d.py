import dispatch.yt
import numpy as np
import matplotlib.pyplot as plt

# gamma in gas law
gamma = 1.4

# load data from Dispatch
run_names = ['sod_bifrost_x',
            'sod_bifrost_y',
            'sod_bifrost_z']
#run outside the python directory inside the experiment
data='data/'

i = 0
axis = ['x', 'y', 'z']
line = ['-', '--', ':']
ray_list = []
ray_sort_list = []
x = []
rho = []
u = []
ee = []
p = []

for run in run_names:
	ds=dispatch.yt.snapshot(20, run=run, data=data)
	var=axis[i]
	print(var)

	# load ray on x-axis
	ray = ds.ortho_ray(i,(0,0))
	ray_sort = np.argsort(ray[axis[i]])

	ray_list.append(ray)
	ray_sort_list.append(ray_sort)

	# Dispatch quantities
	x.append(np.array(ray[axis[i]][ray_sort]))
	rho.append(np.array(ray['density'][ray_sort]))
	u.append(np.array(ray['velocity_'+axis[i]][ray_sort]))
	ee.append(np.array(ray['ee'][ray_sort]))
	# equation of state
	p.append(rho[i]*(gamma - 1)*ee[i])
	i += 1

print('Quantities done')

#plot density
plt.figure(1)
for i in range(len(axis)):
	plt.plot(x[i], rho[i], ls=line[i], label=axis[i])
#plt.xlabel('')
plt.ylabel(r'$\rho$')
plt.legend()
plt.savefig('sod_rho.png')

#plot pressure
plt.figure(2)
for i in range(len(axis)):
	plt.plot(x[i], p[i], ls=line[i], label=axis[i])
#plt.xlabel('z')
plt.ylabel(r'$p$')
plt.legend()
plt.savefig('sod_p.png')

#plot velocity
plt.figure(3)
for i in range(len(axis)):
	plt.plot(x[i], u[i], ls=line[i], label=axis[i])
plt.ylabel('r$v$')
plt.legend()
plt.savefig('sod_v.png')
