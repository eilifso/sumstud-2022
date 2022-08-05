<script type="text/javascript"
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$'], ['\\(','\\)']],
      processEscapes: true},
      jax: ["input/TeX","input/MathML","input/AsciiMath","output/CommonHTML"],
      extensions: ["tex2jax.js","mml2jax.js","asciimath2jax.js","MathMenu.js","MathZoom.js","AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
      TeX: {
      extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"],
      equationNumbers: {
      autoNumber: "AMS"
      }
    }
  });
</script>

# The Einfeld-1203 strong rarefaction test

In [Einfeldt et al. (1991)](https://www.sciencedirect.com/science/article/pii/0021999191902113), a set of problems designed to test hydrodynamics Riemann solvers are described, and among them is the Einfeldt-1203 test. 
We will compare the quantities we get from the Bifrost and Ramses solvers with figure 11 in [Stone et al.](https://iopscience.iop.org/article/10.1086/588755/pdf) in order to verify the performance of our solvers. 

We begin with the Bifrost solver, using using $\gamma = 1.4$, and simulating until $t=0.1$ s. 

As described in [Stone et al.](https://iopscience.iop.org/article/10.1086/588755/pdf), the initial right and left values are as follows: 

|            	| $\rho$ 	| $v_x$ 	| $v_y$ 	| $v_z$ 	| $P$ 	| $B_x$ 	| $B_z$ 	|
|------------	|----------	|---------	|---------	|---------	|-------	|---------	|---------	|
| Left side  	| 1.0      	| -2.0    	| 0       	| 0       	| 0.4   	| ...     	| ...     	|
| Right side 	| 1.0      	| 2.0     	| 0       	| 0       	| 0.4   	| ...     	| ...     	|

Plotting the resulting density ($\rho$), pressure ($P$), horizontal velocity ($\u_x$) and the specific internal energy scaled by ($\gamma - 1$) ($P/\rho$) in the x- y- and z-direction yields figure 1: 

![image](images/einfeldt/einfeldt_standard.png)

Comparing our plot with figure 11 in [Stone et al.](https://iopscience.iop.org/article/10.1086/588755/pdf), we can immediately see that the x-axis has different values. This should have no effect on the shape of the plots, and we therefore choose not to bother with changing the x-axis to replicate the figure. We also see that the shape of the specific internal energy ($P/\rho$) is different from the reference figure, and that it does not extend down quite as far as it should. 
The reason for this might be that we are plotting the wrong variable, or that it is somehow scaled differently in the paper. 
(We plot the specific internal energy as: `p/rho`, where ``p = rho * (gamma - 1) * ee`. )
However, the pressure and density plots seem to fit the reference figure very nicely, and therefore we assume the results are valid. 

We can examine the time evolution of the einfeldt problem by plotting a specific snapshot. The biggest changes happen in the earliest snapshots, since the system begins in an extreme initial state, which it will very quickly try to even out. 
The following gif shows how the system changes from snapshots 0 (the initial state) to snapshot 20 (the end time $t=0.1$ s.

![gif](images/einfeldt/einfeldt_early_times.gif)

Further on, we can modify each of the Bifrost parameters $\nu_1$, $\nu_2$, $\nu_3$, $\nu_d$, $\nu_{ee}$ and $\eta_3$ in order to fine-tune the solver to better match the results in [Stone et al.](https:    //iopscience.iop.org/article/10.1086/588755/pdf). 
