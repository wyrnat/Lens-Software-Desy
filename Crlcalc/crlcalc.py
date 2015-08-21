try:
    from Werkzeuge import crlcalcWerkzeug
except:
    print "crlcalcWerkzeug missing. Maybe in another directory?"
    exit()

try:
    from Services import spline, abbildungsgeometrie, diffraction, linse
except:
    print "Services or Service Class missing. Please add the package or the file to the path"
    exit()

try:
    from Fachwerte import inputValues, outputValues, valProp, values
except:
    print "Fachwerte or Fachwert Class missing"
    exit()
    
try:
    from UI import crlcalcUI, Observable, gui_builder
except:
    print "UI missing. PLease add the Package to the path"
    exit()

try:
    import wx
except:
    print "wx package missing. Please install wxPython"
    exit()
try:
    import numpy
except:
    print "numpy Package missing. Please install numpy"
    exit()

"""
TODO: WebOffice anschreiben
TODO: Gui umbauen, kein Gridbag mehr
TODO: PySide herunterladen!
TODO: Bilderchen auf Homepage
TODO: Datei mit allen Werten ausgeben (Problem: Serveruebergabe)
TODO: Rekursionslimit neu gesetzt. Wie reagiert der Server?
TODO: GetFieldOut(In)putValue vereinigen
"""

app = wx.PySimpleApp()
instance_of_Werkzeug = crlcalcWerkzeug.CrlcalcWerkzeug()
app.MainLoop()



        
