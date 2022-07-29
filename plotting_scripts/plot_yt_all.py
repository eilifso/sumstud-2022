import dispatch.yt
import numpy as np
import matplotlib.pyplot as plt

# gamma in gas law
gamma = 1.4




# load data from Dispatch
run_name = ['sod_bifrost_x', 'sod_bifrost_y', 'sod_bifrost_z']
axes=['x','y','z']
vdir=['ux','uy','uz']
lines = ['--','-.',':']

#run outside the python directory inside the experiment
data='data/'




for i in range(len(run_name)):
    ds = dispatch.yt.snapshot(20, run=run_name[i], data=data)
    ray = ds.ortho_ray(i,(0,0))
    ray_sort = np.argsort(ray[axes[i]])

    # Dispatch quantities
    x = np.array(ray[axes[i]][ray_sort])

    rho = np.array(ray['gas','density'][ray_sort])
    u_x = np.array(ray['gas','velocity_'+axes[i]][ray_sort])
    ee = np.array(ray['stream','ee'][ray_sort])
    # equation of state
    p = rho*(gamma - 1)*ee

    #plot density
    plt.figure(1)
    plt.plot(x, rho, label=axes[i],ls=lines[i])
    plt.ylabel(r'$\rho$')
    plt.legend()


    #plot pressure
    plt.figure(2)
    plt.plot(x, p, label=axes[i],ls=lines[i])
    plt.ylabel(r'$p$')
    plt.legend()

    #plot velocities	
    plt.figure(3)
    plt.plot(x,u_x,label=vdir[i],ls=lines[i])
    plt.ylabel('v')
    plt.legend()

plt.figure(1)
plt.savefig('sod_rho_yt.png')


plt.figure(2)
plt.savefig('sod_p_yt.png')

plt.figure(3)
plt.savefig('sod_v_yt.png')
