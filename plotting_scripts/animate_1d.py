import dispatch.yt
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# gamma in gas law
gamma = 1.4	

# load data from Dispatch
#run_names = ['sod_bifrost_x',
#		'sod_bifrost_y',
#		'sod_bifrost_z']
#experiment = 'brio-wu_bifrost'
#experiment = 'rj4d_'
#run_names = []
	#directions = ['x', 'density', 'U',
#		'Uv', 'e', 'E', 
#		'Ca']
#directions = ['x']
#directions.append(sys.argv[1])
#for dir in directions:
#	run_names.append(f'{experiment}{dir}')
run_names = ['rj4d_x']
for name in sys.argv[1:]:
	run_names.append(name)
print(run_names)
	

#run_names = ['brio-wu_bifrost_x',
#	     'brio-wu_bifrost_y',
#	     'brio-wu_bifrost_z']
#end = 11  # 10 dirs in 
#run outside the python directory inside the experiment
data='data/'
end = len(next(os.walk(f'{data}{run_names[0]}'))[1])-1
print(end)

i = 0
#axis = ['x', 'y', 'z']
axis = ['x']*len(run_names)
print(axis)
line = ['-', '--', ':', '-.', 'dotted', 'dashdot', 'solid', 'dashed']
ray_list = []
ray_sort_list = []
x = []
rho = []
u = []
ee = []
p = []
label = []

fig_name = run_names[0].replace('_x','')
for iout in range(end):
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
		# equation of state
		p.append(rho[i]*(gamma - 1)*ee[i])
		label.append('_'.join(run_names[i].split('_')[1:]))
		i += 1
		
	print('Quantities done')
	#plot density
	label[0] = 'Original'
	plt.figure(1)
	for i in range(len(run_names)):
		plt.plot(x[i], rho[i], ls=line[i], label=label[i])
		#plt.plot(x[i], rho[i], ls=line[i], label=axis[i])
	plt.xlabel('x')
	plt.ylabel(r'$\rho$')
	plt.title(f'iout={iout}, t=[0,0.20]s')
	plt.legend()
	plt.savefig(f'{fig_name}_rho_{iout}.png')
	plt.close()
	
	#plot pressure
	plt.figure(2)
	for i in range(len(run_names)):
		plt.plot(x[i], p[i], ls=line[i], label=label[i])
		#plt.plot(x[i], p[i], ls=line[i], label=axis[i])
	plt.xlabel('x')
	plt.ylabel(r'$p$')
	plt.title(f'iout={iout}, t=[0,0.20]s')
	plt.legend()
	#plt.savefig('sod_p.png')
	plt.savefig(f'{fig_name}_p_{iout}.png')
	plt.close()	
	
	#plot velocity
	plt.figure(3)
	for i in range(len(run_names)):
		plt.plot(x[i], u[i], ls=line[i], label=label[i])
		#plt.plot(x[i], u[i], ls=line[i], label=axis[i])
	plt.xlabel('x')
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
