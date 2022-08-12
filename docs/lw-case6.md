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


* Current branch: develop-bc
* Current commit: 34c177c
# Liska and Wendroff case 6

## Initial parameters
|       	| Left  	|          	|           	|           	| Right 	|          	|           	|           	|
|-------	|-------	|----------	|-----------	|-----------	|-------	|----------	|-----------	|-----------	|
|       	| $P_l$ 	| $\rho_l$ 	| $v_{x,l}$ 	| $v_{y,l}$ 	| $P_r$ 	| $\rho_r$ 	| $v_{x,r}$ 	| $v_{y,r}$ 	|
| Upper 	| 1.0   	| 2.0      	| 0.75    	| 0.5       	| 1.0   	| 1.0   	| 0.75       	| -0.5|
| Lower 	| 1.0   	| 1.0      	| -0.75       	| 0.5       	| 1.0   	| 3.0      	| -0.75       	| -0.5    	|


 And produces the following end time plots for the end time


 ![img](images/2D/case6/pressure_lw_case6_xy_3.png)


Which is close to the [Fig 4.3](https://rsaa.anu.edu.au/files/liska_wendroff_2003.pdf)(Liska and Wendroff, 2003), if we look at the corresponding regime.

If we plot for the same but with a 128x128 grid we get the following


![img](images/2D/case6/pressure_og_lw_case6_xy_3.png)


Which has the same form as the 400x400 grid, but the spirals are less defines. 


## yz and zx planes

By permutating the cordinates we can reproduce in the $$yz$$ and $$zx$$ planes, and they should look identical. 
They don't. 
The **.nml** files can be found in the corresponding github repo. 
But one must first permutate, then switch the coordinates of the plane one is looking at. 
e.g $$y\leftrightarrow z$$. 
Then we will still get a transposed image, but the general form is there.


 ![img](images/2D/case6/pressure_lw_case6_yz_1.png)
 ![img](images/2D/case6/pressure_lw_case6_zx_2.png)
