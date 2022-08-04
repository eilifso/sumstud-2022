import dispatch.yt
import numpy as np
import matplotlib.pyplot as plt
import sys

# gamma in gas law
gamma = 1.4	

run_names = ['rj4d_x']
for name in sys.argv[1:]:
	run_names.append(name)
iout = 18 
#run outside the python directory inside the experiment
data='data/'

i = 0
#axis = ['x', 'y', 'z']
axis = ['x', 'x', 'x']
line = ['-.', '--', ':']
ray_list = []
ray_sort_list = []
x = []
rho = []
u = []
ee = []
p = []
mag = []
label = []
for run in run_names:
	ds=dispatch.yt.snapshot(iout=iout, run=run, data=data)
	var=axis[i]
	print(var)

	# load ray on x-axis
	ray = ds.ortho_ray(0,(0,0))
	ray_sort = np.argsort(ray[axis[i]])

	ray_list.append(ray)
	ray_sort_list.append(ray_sort)
	
	# Dispatch quantities
	x.append(np.array(ray[axis[i]][ray_sort]))
	rho.append(np.array(ray['density'][ray_sort]))
	u.append(np.array(ray['velocity_'+axis[i]][ray_sort]))
	ee.append(np.array(ray['ee'][ray_sort]))
	#mag.append(np.array(ray['magnetic_'+axis[i]][ray_sort]))
	# equation of state
	p.append(rho[i]*(gamma - 1)*ee[i])
	label.append(run_names[i].split('_')[-1])
	if label[i] == 'density':
		label[i] = r'$\rho$'
	i += 1
	
print('Quantities done')
#fig_name = run_names[0].replace('_x','')
fig_name = sys.argv[1]
label[0] = 'Original'
#plot density
plt.figure(1)
for i in range(len(run_names)):
	plt.plot(x[i], rho[i], ls=line[i], label=label[i])
plt.xlabel(r'$x$')
plt.ylabel(r'$\rho$')
plt.legend()
plt.savefig(fig_name+'_rho.png')

#plot pressure
plt.figure(2)
for i in range(len(run_names)):
	plt.plot(x[i], p[i], ls=line[i], label=label[i])
plt.xlabel(r'$x$')
plt.ylabel(r'$p$')
plt.legend()
#plt.savefig('sod_p.png')
plt.savefig(fig_name+'_p.png')

#plot velocity
plt.figure(3)
for i in range(len(run_names)):
	plt.plot(x[i], u[i], ls=line[i], label=label[i])
plt.xlabel(r'$x$')
plt.ylabel(r'$v$')
plt.legend()
#plt.savefig('sod_v.png')
plt.savefig(fig_name+'_v.png')

#plt.figure(4)
#for i in range(len(run_names)):
#	plt.plot(x[i], p[i], ls=line[i], label=axis[i])
#plt.ylabel(r'$B$')
#plt.legend()
#plt.savefig('brio-wu_mag.png')
