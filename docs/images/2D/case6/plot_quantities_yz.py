import dispatch
import dispatch.select as ds
import dispatch.graphics as dg
import dispatch.yt as dyt
import yt as yt
from yt.units import dimensions
import matplotlib.pyplot as plt
import numpy as np
import sys


data='data/'
#run = 'lw_case3_xy'
#run = 'lw_case6_xy'
#run = 'lw_case17_xy'
run = sys.argv[1]
idir = 1 # The direction of the 2D surface (I.e. the axis normal to it)

field='pressure'
# Note: The field 'pressure' doesn't exist yet.

# Load dataset
ds = dyt.open_amr(iout=3,run=run,data=data,verbose=0)

# Create the derived field 'pressure'.
# It is derived from the equation of state using the fields
# 'density' and 'ee' (energy).
ad = ds.all_data()

def _pressure(field, ad):
	return (ad.ds.gamma - 1)*ad['stream', 'density']*ad['stream', 'ee']\
		/ds.units.s**2*ds.units.cm**2 
# For unknown reasons 'ee' does not have any units. Consequently I have 
# added the units seconds^{-2}cm^2 to the equation above

ds.add_field(
	name=('gas', 'pressure'),
	function=_pressure,
	sampling_type="local",
	units='g/(cm*s**2)')
	#units='auto', # This line and the next is used instead of the 
		       # previous one to let yt automate units
	#dimensions=dimensions.pressure)

# Make a sliceplot of the pressure
slc = yt.SlicePlot(ds=ds, axis='x', fields=[field])
slc.set_cmap(field, "jet")
slc.set_log(field, False)
# Overplot density contours
if run == 'lw_case6_yz':
	slc.annotate_contour(("gas", "density"), ncont=29, clim=(0.25, 3.05))
	slc.set_zlim('pressure', 0.1, 1.1)  
elif run == 'lw_case3_yz':
	slc.annotate_contour(("gas", "density"), ncont=32, clim=(0.16, 1.71))
	slc.set_zlim('pressure', 0.1, 1.8)  
elif run == 'lw_case17_yz':
	slc.annotate_contour(("gas", "density"), ncont=30, clim=(0.53, 1.98))
	slc.set_zlim('pressure', 0.1, 1.2)  
# Overplot velocity field
slc.annotate_quiver(('gas', 'velocity_y'), ('gas', 'velocity_z'))
# Add timestamp
slc.annotate_timestamp(draw_inset_box=True)
slc.annotate_title('Density contours and velocity field overlaid pressure')
# And finally, save the figure
slc.save(field+'_'+run+'_'+str(idir)+'.png')

