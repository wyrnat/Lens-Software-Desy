CrlCalc - Compound Refractive Lens Calculation Software
*******************************************************
-Based on the Java Software of Jens Patommel-

	Author: 	Sven-Jannik Wöhnert
	Contact:	jannik.woehnert@desy.de
	Supervisor:	christian.schroer@desy.de
	Website:	http://crl.desy.de
	
	
Requierements:
	- Python 2 (2.7 recommended)
	- wxPython
	- numpy
	- scipy
	
	
Start:
	Open Command line in "crlcalc.py" directory
	Enter "python crlcalc.py"
	

Runtime:
	- fill beamline values in the yellow fields
	- Choose material and adjust density if necessary.
	- For non-listed material, choose "CUSTOM" as material
	  and fill green fields with the specific values
	- Save your input and output Data into "params.dat", the
	  data will load the next time the software is started
	- If Crlcalc is not calculating, read the error message at the bottom
	  of the Interface
	  
Adding new materials:
	- create delta and mu value data file -> "XXXd.dat", "XXXMu.dat"
		- fill in the values for Energy [500eV, 200000eV] in steps of 500eV,
	  	  separated by ","
	  	- save both files in "Services/elementdata/"
	- open "Fachwerte/materials.py" and add at the end of the arrays
		- the material name
		- name of "XXXd.dat"
		- name of "XXXMu.dat"
		- default material density