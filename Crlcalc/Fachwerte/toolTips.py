'''
Created on 14.04.2016

@author: Woehnert
'''

"""
TOOLTIP DATA FILE:
This file contains two dict objects containing
all parameter information which will be displayed
in the gui as tooltips
"""

inTips = {'energy': "Beam energy \n limited from 500ev to 200keV",
          'wavelength': "Beam wavelength \n ",
          'b_v': "Source size vertical",
          'b_h': "Source size horizontal",              
          'g': "Distance between Source and Mirror Plane",                          
          'dpsf': "Data point spread function",                              
          'intensity': "Beam intensity",                      
          'R': "Lens curvature \n Radius of virtual sphere on central point of the lens",                                
          'R_0': "curvature expansion \n 2*R_0 equals the lens height",                           
          'lockR0toW': "lock r_0 to W for a symmetric sphere",
          'd': "lens thickness at the tightest point",                                
          'N': "Number of lenses in line",                              
          'rough': "Root Mean squared roughness of the lens surface",                          
          'W': "thickness of complete lens in beam direction",
          'material_choice': "Choose a lens material for delta and mu calculation",
          'density': "lens material density",                          
          'delta': "index of refraction divided by material density",
          'mu': "mass attenuation effect value divided by material densitys"
          }

outTips = {'f': "focus point distance to the source",          
           'H': "position of principal plane in relation to the mirror plane" ,             
           'Deff': "effective aperture for diffraction and roughness",       
           'NA': "Numeric aperture",
           'T_p': "Transmission",
           'CrossSection': "Cross Section",  
           'b': "Distance between mirror plane and Image",         
           'L1': "Distance between Source and principle plane",    
           'L2': "Distance between principle plane and Image",    
           'ISh': "Image Size horizontal",          
           'ISv': "image Size vertical",            
           'magn': "magnification of the Image Setup",
           'gain': "Intensity gain",
           'flux': "Photon flux \n cross section times the intensity",         
           'diff_limit': "Diffraction limit",     
           'dof': "depth of field",           
           'mb_dof': "Depth of Field for the microbeam",       
           'ISh_corr': "Image size horizontal \n corrected for above named pertubations",     
           'ISv_corr': "Image size vertical \n corrected for above named pertubations",     
           'gain_corr': "Intensity gain \n corrected for above named pertubations"
           }