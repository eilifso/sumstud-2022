# Torrilhon test

For the Torrilhon(2003) test we use the parameter values from table 2 in James M.Stone et al 2008 ApJS 178 137) as follows

|$$\rho_R$$|$$P_R$$|$$B_{y,R}$$|$$B_{z,R}$$|$$\rho_R$$|$$P_R$$|$$B_{y,R}$$|$$B_{z,R}$$|$$v_i$$ |$$\gamma$$|
|----------|-------|-----------|-----------|----------|-------|-----------|-----------|--------|----------|
|1.0	   | 1.0   | 1.0       | 0         | 0.2      | 0.2   | cos(3)    | sin(3)    | 0      | 1.4      |

Using the stagger2/bifrost solver with end_time=0.1 and timestep=0.01 yields the following plots

![rho](images/Torrilhon_bifrost_rho.png)
![B](images/Torrilhon_bifrost_Bd.png)
![v](images/Torrilhon_bifrost_ud.png)
