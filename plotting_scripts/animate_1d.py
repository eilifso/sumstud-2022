# To convert all the png to a gif I use the below terminal command
# convert -delay 20 'foo%d.png[X-Y]' -loop 0 bar.gif
# Where 
# foo is the png file name
# X is the start number, e.g 0
# Y is the end number, e.g 20
# bar is the file name of the gif

import dispatch.yt
import numpy as np
import matplotlib.pyplot as plt
import os

# gamma in gas law
gamma = 1.4

# load data from Dispatch
#experiment = 'brio-wu_bifrost'
experiment = 'rj4d'
run_names = []
directions = ['_x', '_y', '_z']
for dir in directions:
	run_names.append(f'{experiment}{dir}')
print(run_names)

data='data/'
end = len(next(os.walk(f'{data}{run_names[0]}'))[1])-1
print(end)

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

fig_name = run_names[0].replace('_x','')
for iout in range(end):
	for run in run_names:
		ds=dispatch.yt.snapshot(iout=iout, run=run, data=data)
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
	for i in range(len(run_names)):
		plt.plot(x[i], rho[i], ls=line[i], label=axis[i])
	#plt.xlabel('')
	plt.ylabel(r'$\rho$')
	plt.title(f'iout={iout}, t=[0,0.20]s')
	plt.legend()
	plt.savefig(f'{fig_name}_rho_{iout}.png')
	plt.close()

	#plot pressure
	plt.figure(2)
	for i in range(len(run_names)):
		plt.plot(x[i], p[i], ls=line[i], label=axis[i])
	#plt.xlabel('z')
	plt.ylabel(r'$p$')
	plt.title(f'iout={iout}, t=[0,0.20]s')
	plt.legend()
	#plt.savefig('sod_p.png')
	plt.savefig(f'{fig_name}_p_{iout}.png')
	plt.close()

	#plot velocity
	plt.figure(3)
	for i in range(len(run_names)):
		plt.plot(x[i], u[i], ls=line[i], label=axis[i])
	plt.ylabel(r'$v$')
	plt.title(f'iout={iout}, t=[0,0.20]s')
	plt.legend()
	#plt.savefig('sod_v.png')
	plt.savefig(f'{fig_name}_v_{iout}.png')
	plt.close()


	ray_list.clear()
	ray_sort_list.clear()
	x.clear()
	rho.clear()
	u.clear()
	ee.clear()
	p.clear()
	i = 0
