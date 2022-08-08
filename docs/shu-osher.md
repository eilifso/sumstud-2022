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


# Shu Osher test

We will be comparing our solvers' solutions to the Shu-Osher test with the plots provided by the University of Rochester in their [report on hydrodynamics test problems](https://flash.rochester.edu/site/flashcode/user_support/flash_ug_devel/node184.html#Fig:Shu-Osher_reference_solution). AS a reference, they provided these figures of the density, x-velocity and pressure in the x-direction. 

![foo](images/shu-osher/reference_shu-osher.png)

The Shu-Osher test uses the initial values: 

|            	| $$\rho$$               	| $$v_x$$  	| $$v_y$$ 	| $$v_z$$ 	| $$P$$   	| $$B_x$$ 	| $$B_z$$ 	|
|------------	|------------------------	|----------	|---------	|---------	|---------	|---------	|---------	|
| Left side  	| 3.857143               	| 2.629369 	| 0       	| 0       	| 10.3333 	| ...     	| ...     	|
| Right side 	| $$1+0.2 \sin(5\pi x)$$ 	| 0        	| 0       	| 0       	| 1       	| ...     	| ...     	|

### Bifrost 

Reproducing the test using our Bifrost solver with standard configuration (and simultaneously testing the x-, y- and z-directions) yields the result: 
![shu-osher](images/shu-osher/xyz.png)

Here we have used $t = 1.8$ s as the end time of the simulation. We can see that our Bifrost solution of the Shu-Osher test replicates the reference figure very accurately. 

The time evolution of the Shu-Osher test in the x-, y- and z-directions very nicely shows us the shock wave travelling along the x-axis: 

![foo](images/shu-osher/time_evolution.gif)


