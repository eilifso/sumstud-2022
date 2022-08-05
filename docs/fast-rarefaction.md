<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>
# Fast rarefaction test

* Hash: 177f0c9
* Branch: development-bc

## Bifrost

Using the initial conditions stated in **<++> insert ref here<++>** 

|$$\rho_L$$|$$v_{x,L}$$|$$v_{y,L}$$|$$v_{z,L}$$|$$P_L$$|$$B_{y,L}$$|$$B_{z,L}$$|$$\rho_R$$|$$v_{x,R}$$|$$v_{y,R}$$|$$v_{z,R}$$|$$P_R$$|$$B_{y,R}$$|$$B_{z,R}$$|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|-2|0|0|0.45|0.5|0|1|2|0|0|0.45|0.5|0|

I get the following animations 


![ani](images/fast_raref/og/rj4d_p.gif)
![ani](images/fast_raref/og/rj4d_v.gif)
![ani](images/fast_raref/og/rj4d_rho.gif)


For the still picture for the same time as the refrence.  


![img](images/fast_raref/og/rj4d_p_16.png)
![img](images/fast_raref/og/rj4d_v_16.png)
![img](images/fast_raref/og/rj4d_rho_16.png)


Where we observe that the velocity plot is a bit diffrenent then the figure 5 in (**ADD HERE**) 


Will now tweak the parameteres. 
Here I ran into a problem that for the **eta3** parameter. 
That the whole program would crash for a higher value, so have neglected that for the following. 

![gif](images/fast_raref/changes/rj4d_p.gif)
![gif](images/fast_raref/changes/rj4d_v.gif)
![gif](images/fast_raref/changes/rj4d_rho.gif)

Still pictures

![img](images/fast_raref/changes/rj4d_p_16.png)
![img](images/fast_raref/changes/rj4d_v_16.png)
![img](images/fast_raref/changes/rj4d_rho_16.png)


## Ramses
The original animation from the ramses are


![ani](images/fast_raref/ramses_og/rj4d_p.gif)
![ani](images/fast_raref/ramses_og/rj4d_v.gif)
![ani](images/fast_raref/ramses_og/rj4d_rho.gif)
