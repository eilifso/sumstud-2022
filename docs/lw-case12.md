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

# Liska and Wendroff case 12

Case 12 in [Liska and Wendroff (2003)](https://rsaa.anu.edu.au/files/liska_wendroff_2003.pdf) describes a Riemann problem with the intial values: 

|       	| Left  	|          	|           	|           	| Right 	|          	|           	|           	|
|-------	|-------	|----------	|-----------	|-----------	|-------	|----------	|-----------	|-----------	|
|       	| $P_l$ 	| $\rho_l$ 	| $v_{x,l}$ 	| $v_{y,l}$ 	| $P_r$ 	| $\rho_r$ 	| $v_{x,r}$ 	| $v_{y,r}$ 	|
| Upper 	| 1.0   	| 1.0      	| 0.7276    	| 0.0       	| 0.4   	| 0.5313   	| 0.0       	| 0.0       	|
| Lower 	| 1.0   	| 0.8      	| 0.0       	| 0.0       	| 1.0   	| 0.0      	| 0.0       	| 0.7276    	|

We will run this test with the parameters described above, plotting the final time $t=0.25$ s and comparing with the corresponding reference figure in [Liska and Wendroff (2003)](https://rsaa.anu.edu.au/files/liska_wendroff_2003.pdf). 
