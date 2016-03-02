# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BuilderFrame
###########################################################################

class BuilderFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CRLcalc - Offline Test Version 2.2 (2/3/2106)", pos = wx.DefaultPosition, size = wx.Size( 987,820 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer451 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		fgSizer1 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.Panel_XRay = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.Panel_XRay, wx.ID_ANY, u"X-Ray Source and Detector" ), wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"energy:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetToolTipString( u"beam energy" )
		
		bSizer6.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.Field_Energy = wx.TextCtrl( self.Panel_XRay, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RICH )
		self.Field_Energy.SetMaxLength( 0 ) 
		self.Field_Energy.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.Field_Energy.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_Energy.SetToolTipString( u"beam energy" )
		
		bSizer6.Add( self.Field_Energy, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"eV", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText113 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"wavelength:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText113.Wrap( -1 )
		self.m_staticText113.SetToolTipString( u"beam wavelength" )
		
		bSizer61.Add( self.m_staticText113, 0, wx.ALL, 5 )
		
		self.Field_WaveLength = wx.TextCtrl( self.Panel_XRay, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_WaveLength.SetMaxLength( 0 ) 
		self.Field_WaveLength.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.Field_WaveLength.SetToolTipString( u"beam wavelength" )
		
		bSizer61.Add( self.Field_WaveLength, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"Å", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer61.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer61, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.Panel_XRay, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer67 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText17 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"Source Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer67.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer67, 0, wx.EXPAND, 5 )
		
		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText12 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"horizontal:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer62.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.Field_SSh = wx.TextCtrl( self.Panel_XRay, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_SSh.SetMaxLength( 0 ) 
		self.Field_SSh.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		
		bSizer62.Add( self.Field_SSh, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer62.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer62, 0, wx.EXPAND, 5 )
		
		bSizer63 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"vertical:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer63.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.Field_SSv = wx.TextCtrl( self.Panel_XRay, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_SSv.SetMaxLength( 0 ) 
		self.Field_SSv.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		
		bSizer63.Add( self.Field_SSv, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer63.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer63, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.Panel_XRay, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer64 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText14 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"g", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetToolTipString( u"distance between source and mirror plane" )
		
		bSizer64.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.Field_g = wx.TextCtrl( self.Panel_XRay, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_g.SetMaxLength( 0 ) 
		self.Field_g.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_g.SetToolTipString( u"distance between source and mirror plane" )
		
		bSizer64.Add( self.Field_g, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer64.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer64, 0, wx.EXPAND, 5 )
		
		bSizer65 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText15 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"I", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetToolTipString( u"Intensity of the beam" )
		
		bSizer65.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.Field_Intensity = wx.TextCtrl( self.Panel_XRay, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_Intensity.SetMaxLength( 0 ) 
		self.Field_Intensity.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_Intensity.SetToolTipString( u"Intensity of the beam" )
		
		bSizer65.Add( self.Field_Intensity, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"Photons/(s * mm^2)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer65.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer65, 0, wx.EXPAND, 5 )
		
		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"dpsf", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.Hide()
		self.m_staticText16.SetToolTipString( u"detector point spread function:\nresolving capacity of the detector for focus determination" )
		self.m_staticText16.SetMaxSize( wx.Size( 100,-1 ) )
		
		bSizer66.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.Field_dpsf = wx.TextCtrl( self.Panel_XRay, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_dpsf.SetMaxLength( 0 ) 
		self.Field_dpsf.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_dpsf.Hide()
		
		bSizer66.Add( self.Field_dpsf, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.Panel_XRay, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		self.m_staticText26.Hide()
		
		bSizer66.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer66, 0, wx.EXPAND, 5 )
		
		
		bSizer5.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		
		self.Panel_XRay.SetSizer( bSizer5 )
		self.Panel_XRay.Layout()
		bSizer5.Fit( self.Panel_XRay )
		fgSizer1.Add( self.Panel_XRay, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel7 = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, u"Compound Refractive Lens Structure" ), wx.VERTICAL )
		
		bSizer651 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText151 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"R:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText151.Wrap( -1 )
		self.m_staticText151.SetToolTipString( u"lens curvature:\nradius of virtual sphere on the central point of the lens" )
		
		bSizer651.Add( self.m_staticText151, 0, wx.ALL, 5 )
		
		self.Field_R = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_R.SetMaxLength( 0 ) 
		self.Field_R.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_R.SetToolTipString( u"lens curvature:\nradius of virtual sphere on the central point of the lens" )
		
		bSizer651.Add( self.Field_R, 0, wx.ALL, 5 )
		
		self.m_staticText251 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )
		bSizer651.Add( self.m_staticText251, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer651, 0, wx.EXPAND, 5 )
		
		bSizer652 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText152 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"R_0:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText152.Wrap( -1 )
		self.m_staticText152.SetToolTipString( u"2*R_0 = lens height" )
		
		bSizer652.Add( self.m_staticText152, 0, wx.ALL, 5 )
		
		self.Field_R_0 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_R_0.SetMaxLength( 0 ) 
		self.Field_R_0.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_R_0.SetToolTipString( u"2*R_0 = lens height" )
		
		bSizer652.Add( self.Field_R_0, 0, wx.ALL, 5 )
		
		self.m_staticText252 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText252.Wrap( -1 )
		bSizer652.Add( self.m_staticText252, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer652, 0, wx.EXPAND, 5 )
		
		bSizer653 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer653.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Check_RWLock = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"lock R_0 to W", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Check_RWLock.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Check_RWLock.SetToolTipString( u"R_0 depending on thickness (W) and curvature (R)" )
		
		bSizer653.Add( self.Check_RWLock, 0, wx.ALL, 5 )
		
		
		bSizer653.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer4.Add( bSizer653, 0, wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer4.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer654 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText154 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"d:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText154.Wrap( -1 )
		self.m_staticText154.SetToolTipString( u"lens thickness at the tightest point" )
		
		bSizer654.Add( self.m_staticText154, 0, wx.ALL, 5 )
		
		self.Field_d = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_d.SetMaxLength( 0 ) 
		self.Field_d.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_d.SetToolTipString( u"lens thickness at the tightest point" )
		
		bSizer654.Add( self.Field_d, 0, wx.ALL, 5 )
		
		self.m_staticText254 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText254.Wrap( -1 )
		bSizer654.Add( self.m_staticText254, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer654, 0, wx.EXPAND, 5 )
		
		bSizer655 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText155 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"N:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText155.Wrap( -1 )
		self.m_staticText155.SetToolTipString( u"Number of lenses" )
		
		bSizer655.Add( self.m_staticText155, 0, wx.ALL, 5 )
		
		self.Field_N = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_N.SetMaxLength( 0 ) 
		self.Field_N.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_N.SetToolTipString( u"Number of lenses" )
		
		bSizer655.Add( self.Field_N, 0, wx.ALL, 5 )
		
		self.m_staticText255 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"#Lenses", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText255.Wrap( -1 )
		bSizer655.Add( self.m_staticText255, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer655, 0, wx.EXPAND, 5 )
		
		bSizer656 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText156 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"roughness", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText156.Wrap( -1 )
		self.m_staticText156.SetToolTipString( u"roughness on lens surface" )
		
		bSizer656.Add( self.m_staticText156, 0, wx.ALL, 5 )
		
		self.Field_rough = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_rough.SetMaxLength( 0 ) 
		self.Field_rough.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_rough.SetToolTipString( u"roughness on lens surface" )
		
		bSizer656.Add( self.Field_rough, 0, wx.ALL, 5 )
		
		self.m_staticText256 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText256.Wrap( -1 )
		bSizer656.Add( self.m_staticText256, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer656, 0, wx.EXPAND, 5 )
		
		bSizer6561 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1561 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"W:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText1561.Wrap( -1 )
		self.m_staticText1561.SetToolTipString( u"lens thickness (in beam direction)" )
		
		bSizer6561.Add( self.m_staticText1561, 0, wx.ALL, 5 )
		
		self.Field_W = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_W.SetMaxLength( 0 ) 
		self.Field_W.SetBackgroundColour( wx.Colour( 251, 252, 148 ) )
		self.Field_W.SetToolTipString( u"lens thickness (in beam direction)" )
		
		bSizer6561.Add( self.Field_W, 0, wx.ALL, 5 )
		
		self.m_staticText2561 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2561.Wrap( -1 )
		bSizer6561.Add( self.m_staticText2561, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer6561, 0, wx.EXPAND, 5 )
		
		
		self.m_panel7.SetSizer( sbSizer4 )
		self.m_panel7.Layout()
		sbSizer4.Fit( self.m_panel7 )
		fgSizer1.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.Panel_CRLens = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.Panel_CRLens, wx.ID_ANY, u"Lens Material" ), wx.VERTICAL )
		
		bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer46.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		Box_MaterialChoices = [ u"Al", u"Al203", u"B", u"Be", u"B4C", u"C", u"Li", u"LiF", u"Mg", u"Ni", u"PC", u"PEEK", u"Si", u"Custom" ]
		self.Box_Material = wx.Choice( self.Panel_CRLens, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Box_MaterialChoices, 0 )
		self.Box_Material.SetSelection( 3 )
		bSizer46.Add( self.Box_Material, 0, wx.ALL, 5 )
		
		
		bSizer46.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( bSizer46, 0, wx.EXPAND, 5 )
		
		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText18 = wx.StaticText( self.Panel_CRLens, wx.ID_ANY, u"Density", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetToolTipString( u"density of lens material" )
		
		bSizer68.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.Field_Density = wx.TextCtrl( self.Panel_CRLens, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_Density.SetMaxLength( 0 ) 
		self.Field_Density.SetBackgroundColour( wx.Colour( 209, 252, 148 ) )
		self.Field_Density.SetToolTipString( u"density of lens material" )
		
		bSizer68.Add( self.Field_Density, 0, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self.Panel_CRLens, wx.ID_ANY, u"g/cm^3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		bSizer68.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( bSizer68, 0, wx.EXPAND, 5 )
		
		bSizer69 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self.Panel_CRLens, wx.ID_ANY, u"delta/rho", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetToolTipString( u"index of refraction divided by the material density" )
		
		bSizer69.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.Field_delta = wx.TextCtrl( self.Panel_CRLens, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_delta.SetMaxLength( 0 ) 
		self.Field_delta.SetBackgroundColour( wx.Colour( 209, 252, 148 ) )
		self.Field_delta.SetToolTipString( u"index of refraction divided by the material density" )
		
		bSizer69.Add( self.Field_delta, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self.Panel_CRLens, wx.ID_ANY, u"cm^3/g", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer69.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( bSizer69, 0, wx.EXPAND, 5 )
		
		bSizer610 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText110 = wx.StaticText( self.Panel_CRLens, wx.ID_ANY, u"mu/rho", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText110.Wrap( -1 )
		self.m_staticText110.SetToolTipString( u"mass attenuation coefficient" )
		
		bSizer610.Add( self.m_staticText110, 0, wx.ALL, 5 )
		
		self.Field_mu = wx.TextCtrl( self.Panel_CRLens, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_mu.SetMaxLength( 0 ) 
		self.Field_mu.SetBackgroundColour( wx.Colour( 209, 252, 148 ) )
		self.Field_mu.SetToolTipString( u"mass attenuation coefficient" )
		
		bSizer610.Add( self.Field_mu, 0, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.Panel_CRLens, wx.ID_ANY, u"cm^2/g", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		bSizer610.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( bSizer610, 0, wx.EXPAND, 5 )
		
		bSizer461 = wx.BoxSizer( wx.VERTICAL )
		
		self.Button_Save = wx.Button( self.Panel_CRLens, wx.ID_ANY, u"Save current configuration", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer461.Add( self.Button_Save, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		sbSizer2.Add( bSizer461, 0, wx.EXPAND, 5 )
		
		
		self.Panel_CRLens.SetSizer( sbSizer2 )
		self.Panel_CRLens.Layout()
		sbSizer2.Fit( self.Panel_CRLens )
		fgSizer1.Add( self.Panel_CRLens, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.Panel_LensProp = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.Panel_LensProp, wx.ID_ANY, u"Lens Properties" ), wx.VERTICAL )
		
		bSizer661 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText161 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"f:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText161.Wrap( -1 )
		self.m_staticText161.SetToolTipString( u"distance bewteen principle plane and focus" )
		
		bSizer661.Add( self.m_staticText161, 0, wx.ALL, 5 )
		
		self.Field_f = wx.TextCtrl( self.Panel_LensProp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_f.SetMaxLength( 0 ) 
		self.Field_f.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.Field_f.SetToolTipString( u"distance bewteen principle plane and focus" )
		
		bSizer661.Add( self.Field_f, 0, wx.ALL, 5 )
		
		self.m_staticText261 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText261.Wrap( -1 )
		bSizer661.Add( self.m_staticText261, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer661, 0, wx.EXPAND, 5 )
		
		bSizer662 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText162 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"H:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText162.Wrap( -1 )
		self.m_staticText162.SetToolTipString( u"difference between mirror plane and principle plane" )
		
		bSizer662.Add( self.m_staticText162, 0, wx.ALL, 5 )
		
		self.Field_H = wx.TextCtrl( self.Panel_LensProp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_H.SetMaxLength( 0 ) 
		self.Field_H.SetToolTipString( u"difference between mirror plane and principle plane" )
		
		bSizer662.Add( self.Field_H, 0, wx.ALL, 5 )
		
		self.m_staticText262 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText262.Wrap( -1 )
		bSizer662.Add( self.m_staticText262, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer662, 0, wx.EXPAND, 5 )
		
		bSizer663 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText163 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"D_eff", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText163.Wrap( -1 )
		self.m_staticText163.SetToolTipString( u"effective aperture for diffraction and roughness" )
		
		bSizer663.Add( self.m_staticText163, 0, wx.ALL, 5 )
		
		self.Field_Deff = wx.TextCtrl( self.Panel_LensProp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_Deff.SetMaxLength( 0 ) 
		self.Field_Deff.SetToolTipString( u"effective aperture for diffraction and roughness" )
		
		bSizer663.Add( self.Field_Deff, 0, wx.ALL, 5 )
		
		self.m_staticText263 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText263.Wrap( -1 )
		bSizer663.Add( self.m_staticText263, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer663, 0, wx.EXPAND, 5 )
		
		bSizer664 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText164 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"N.A.:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText164.Wrap( -1 )
		self.m_staticText164.SetToolTipString( u"numeric aperture" )
		
		bSizer664.Add( self.m_staticText164, 0, wx.ALL, 5 )
		
		self.Field_NA = wx.TextCtrl( self.Panel_LensProp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_NA.SetMaxLength( 0 ) 
		self.Field_NA.SetToolTipString( u"numeric aperture" )
		
		bSizer664.Add( self.Field_NA, 0, wx.ALL, 5 )
		
		self.m_staticText264 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText264.Wrap( -1 )
		bSizer664.Add( self.m_staticText264, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer664, 0, wx.EXPAND, 5 )
		
		bSizer665 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText165 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"T_p", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText165.Wrap( -1 )
		self.m_staticText165.SetToolTipString( u"Transmission" )
		
		bSizer665.Add( self.m_staticText165, 0, wx.ALL, 5 )
		
		self.Field_Tp = wx.TextCtrl( self.Panel_LensProp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_Tp.SetMaxLength( 0 ) 
		self.Field_Tp.SetToolTipString( u"Transmission" )
		
		bSizer665.Add( self.Field_Tp, 0, wx.ALL, 5 )
		
		self.m_staticText265 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText265.Wrap( -1 )
		bSizer665.Add( self.m_staticText265, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer665, 0, wx.EXPAND, 5 )
		
		bSizer666 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText166 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"Cross section", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText166.Wrap( -1 )
		self.m_staticText166.SetToolTipString( u"sigma value of the focus" )
		
		bSizer666.Add( self.m_staticText166, 0, wx.ALL, 5 )
		
		self.Field_CrossSection = wx.TextCtrl( self.Panel_LensProp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_CrossSection.SetMaxLength( 0 ) 
		self.Field_CrossSection.SetToolTipString( u"sigma value of the focus" )
		
		bSizer666.Add( self.Field_CrossSection, 0, wx.ALL, 5 )
		
		self.m_staticText266 = wx.StaticText( self.Panel_LensProp, wx.ID_ANY, u"mm^2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText266.Wrap( -1 )
		bSizer666.Add( self.m_staticText266, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer666, 0, wx.EXPAND, 5 )
		
		
		self.Panel_LensProp.SetSizer( sbSizer3 )
		self.Panel_LensProp.Layout()
		sbSizer3.Fit( self.Panel_LensProp )
		fgSizer1.Add( self.Panel_LensProp, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.Panel_Results = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.Panel_Results, wx.ID_ANY, u"Results for given Geometry" ), wx.VERTICAL )
		
		bSizer611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText111 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"b:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText111.Wrap( -1 )
		self.m_staticText111.SetToolTipString( u"distance between mirror plane and image" )
		
		bSizer611.Add( self.m_staticText111, 0, wx.ALL, 5 )
		
		self.Field_b = wx.TextCtrl( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_b.SetMaxLength( 0 ) 
		self.Field_b.SetToolTipString( u"distance between mirror plane and image" )
		
		bSizer611.Add( self.Field_b, 0, wx.ALL, 5 )
		
		self.m_staticText210 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText210.Wrap( -1 )
		bSizer611.Add( self.m_staticText210, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer611, 0, wx.EXPAND, 5 )
		
		bSizer612 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText112 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"L1:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText112.Wrap( -1 )
		self.m_staticText112.SetToolTipString( u"distance between source and principle plane" )
		
		bSizer612.Add( self.m_staticText112, 0, wx.ALL, 5 )
		
		self.Field_L1 = wx.TextCtrl( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_L1.SetMaxLength( 0 ) 
		self.Field_L1.SetToolTipString( u"distance between source and principle plane" )
		
		bSizer612.Add( self.Field_L1, 0, wx.ALL, 5 )
		
		self.m_staticText211 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		bSizer612.Add( self.m_staticText211, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer612, 0, wx.EXPAND, 5 )
		
		bSizer6411 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1411 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"L2:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText1411.Wrap( -1 )
		self.m_staticText1411.SetToolTipString( u"distance between principle plane and image" )
		
		bSizer6411.Add( self.m_staticText1411, 0, wx.ALL, 5 )
		
		self.Field_L2 = wx.TextCtrl( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_L2.SetMaxLength( 0 ) 
		self.Field_L2.SetToolTipString( u"distance between principle plane and image" )
		
		bSizer6411.Add( self.Field_L2, 0, wx.ALL, 5 )
		
		self.m_staticText2411 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2411.Wrap( -1 )
		bSizer6411.Add( self.m_staticText2411, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer6411, 1, wx.EXPAND, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.Panel_Results, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer11.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer671 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText171 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"Image size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )
		bSizer671.Add( self.m_staticText171, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer671, 1, wx.EXPAND, 5 )
		
		bSizer621 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText121 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"horizontal:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText121.Wrap( -1 )
		bSizer621.Add( self.m_staticText121, 0, wx.ALL, 5 )
		
		self.Field_ISh = wx.TextCtrl( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_ISh.SetMaxLength( 0 ) 
		bSizer621.Add( self.Field_ISh, 0, wx.ALL, 5 )
		
		self.m_staticText221 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		bSizer621.Add( self.m_staticText221, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer621, 0, wx.EXPAND, 5 )
		
		bSizer631 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText131 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"vertical:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText131.Wrap( -1 )
		bSizer631.Add( self.m_staticText131, 0, wx.ALL, 5 )
		
		self.Field_ISv = wx.TextCtrl( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_ISv.SetMaxLength( 0 ) 
		bSizer631.Add( self.Field_ISv, 0, wx.ALL, 5 )
		
		self.m_staticText231 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )
		bSizer631.Add( self.m_staticText231, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer631, 0, wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.Panel_Results, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer11.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer641 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText141 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"magnitude:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText141.Wrap( -1 )
		self.m_staticText141.SetToolTipString( u"magnification of the image setup" )
		
		bSizer641.Add( self.m_staticText141, 0, wx.ALL, 5 )
		
		self.Field_magn = wx.TextCtrl( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_magn.SetMaxLength( 0 ) 
		self.Field_magn.SetToolTipString( u"magnification of the image setup" )
		
		bSizer641.Add( self.Field_magn, 0, wx.ALL, 5 )
		
		self.m_staticText241 = wx.StaticText( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText241.Wrap( -1 )
		bSizer641.Add( self.m_staticText241, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer641, 0, wx.EXPAND, 5 )
		
		bSizer657 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText153 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"gain:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText153.Wrap( -1 )
		bSizer657.Add( self.m_staticText153, 0, wx.ALL, 5 )
		
		self.Field_gain = wx.TextCtrl( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_gain.SetMaxLength( 0 ) 
		bSizer657.Add( self.Field_gain, 0, wx.ALL, 5 )
		
		self.m_staticText253 = wx.StaticText( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText253.Wrap( -1 )
		bSizer657.Add( self.m_staticText253, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer657, 0, wx.EXPAND, 5 )
		
		bSizer667 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText167 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"flux:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText167.Wrap( -1 )
		self.m_staticText167.SetToolTipString( u"cross sections times intensity" )
		
		bSizer667.Add( self.m_staticText167, 0, wx.ALL, 5 )
		
		self.Field_flux = wx.TextCtrl( self.Panel_Results, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_flux.SetMaxLength( 0 ) 
		self.Field_flux.SetToolTipString( u"cross sections times intensity" )
		
		bSizer667.Add( self.Field_flux, 0, wx.ALL, 5 )
		
		self.m_staticText267 = wx.StaticText( self.Panel_Results, wx.ID_ANY, u"Photons/s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText267.Wrap( -1 )
		bSizer667.Add( self.m_staticText267, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer667, 0, wx.EXPAND, 5 )
		
		
		self.Panel_Results.SetSizer( sbSizer11 )
		self.Panel_Results.Layout()
		sbSizer11.Fit( self.Panel_Results )
		fgSizer1.Add( self.Panel_Results, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.Panel_diffraction = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer672 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self.Panel_diffraction, wx.ID_ANY, u"Corrected for diffraction, psf and roughness" ), wx.VERTICAL )
		
		bSizer6611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1611 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"diff. limit:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText1611.Wrap( -1 )
		bSizer6611.Add( self.m_staticText1611, 0, wx.ALL, 5 )
		
		self.Field_DiffLimit = wx.TextCtrl( self.Panel_diffraction, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_DiffLimit.SetMaxLength( 0 ) 
		bSizer6611.Add( self.Field_DiffLimit, 0, wx.ALL, 5 )
		
		self.m_staticText2611 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2611.Wrap( -1 )
		bSizer6611.Add( self.m_staticText2611, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer6611, 0, wx.EXPAND, 5 )
		
		bSizer6621 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1621 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"depth of f.", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText1621.Wrap( -1 )
		bSizer6621.Add( self.m_staticText1621, 0, wx.ALL, 5 )
		
		self.Field_dof = wx.TextCtrl( self.Panel_diffraction, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_dof.SetMaxLength( 0 ) 
		bSizer6621.Add( self.Field_dof, 0, wx.ALL, 5 )
		
		self.m_staticText2621 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2621.Wrap( -1 )
		bSizer6621.Add( self.m_staticText2621, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer6621, 0, wx.EXPAND, 5 )
		
		bSizer66611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16611 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"Corrected Image Size:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText16611.Wrap( -1 )
		bSizer66611.Add( self.m_staticText16611, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer66611, 0, wx.EXPAND, 5 )
		
		bSizer6631 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1631 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"microbeam DOF", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText1631.Wrap( -1 )
		bSizer6631.Add( self.m_staticText1631, 0, wx.ALL, 5 )
		
		self.Field_mdof = wx.TextCtrl( self.Panel_diffraction, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_mdof.SetMaxLength( 0 ) 
		bSizer6631.Add( self.Field_mdof, 0, wx.ALL, 5 )
		
		self.m_staticText2631 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2631.Wrap( -1 )
		bSizer6631.Add( self.m_staticText2631, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer6631, 0, wx.EXPAND, 5 )
		
		bSizer6641 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1641 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"horizontal:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText1641.Wrap( -1 )
		bSizer6641.Add( self.m_staticText1641, 0, wx.ALL, 5 )
		
		self.Field_IShCorr = wx.TextCtrl( self.Panel_diffraction, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_IShCorr.SetMaxLength( 0 ) 
		bSizer6641.Add( self.Field_IShCorr, 0, wx.ALL, 5 )
		
		self.m_staticText2641 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2641.Wrap( -1 )
		bSizer6641.Add( self.m_staticText2641, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer6641, 0, wx.EXPAND, 5 )
		
		bSizer6651 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1651 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"vertical:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText1651.Wrap( -1 )
		bSizer6651.Add( self.m_staticText1651, 0, wx.ALL, 5 )
		
		self.Field_ISvCorr = wx.TextCtrl( self.Panel_diffraction, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_ISvCorr.SetMaxLength( 0 ) 
		bSizer6651.Add( self.Field_ISvCorr, 0, wx.ALL, 5 )
		
		self.m_staticText2651 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2651.Wrap( -1 )
		bSizer6651.Add( self.m_staticText2651, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer6651, 0, wx.EXPAND, 5 )
		
		bSizer6661 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1661 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, u"gain:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText1661.Wrap( -1 )
		bSizer6661.Add( self.m_staticText1661, 0, wx.ALL, 5 )
		
		self.Field_gainCorr = wx.TextCtrl( self.Panel_diffraction, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Field_gainCorr.SetMaxLength( 0 ) 
		bSizer6661.Add( self.Field_gainCorr, 0, wx.ALL, 5 )
		
		self.m_staticText2661 = wx.StaticText( self.Panel_diffraction, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2661.Wrap( -1 )
		bSizer6661.Add( self.m_staticText2661, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer6661, 0, wx.EXPAND, 5 )
		
		
		bSizer672.Add( sbSizer31, 1, wx.EXPAND, 5 )
		
		
		self.Panel_diffraction.SetSizer( bSizer672 )
		self.Panel_diffraction.Layout()
		bSizer672.Fit( self.Panel_diffraction )
		fgSizer1.Add( self.Panel_diffraction, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( fgSizer1 )
		self.m_scrolledWindow1.Layout()
		fgSizer1.Fit( self.m_scrolledWindow1 )
		bSizer451.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer451, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Field_Energy.Bind( wx.EVT_TEXT, self.onEnergyChanged )
		self.Field_SSh.Bind( wx.EVT_TEXT, self.onSSHChanged )
		self.Field_SSv.Bind( wx.EVT_TEXT, self.onSSVChanged )
		self.Field_g.Bind( wx.EVT_TEXT, self.ongChanged )
		self.Field_Intensity.Bind( wx.EVT_TEXT, self.onIChanged )
		self.Field_dpsf.Bind( wx.EVT_TEXT, self.ondpsfChanged )
		self.Field_R.Bind( wx.EVT_TEXT, self.onRChanged )
		self.Field_R_0.Bind( wx.EVT_TEXT, self.onR_0Changed )
		self.Check_RWLock.Bind( wx.EVT_CHECKBOX, self.onCheckChanged )
		self.Field_d.Bind( wx.EVT_TEXT, self.ondChanged )
		self.Field_N.Bind( wx.EVT_TEXT, self.onNChanged )
		self.Field_rough.Bind( wx.EVT_TEXT, self.onroughnessChanged )
		self.Field_W.Bind( wx.EVT_TEXT, self.onWChanged )
		self.Box_Material.Bind( wx.EVT_CHOICE, self.onChangeMaterial )
		self.Field_Density.Bind( wx.EVT_TEXT, self.onDensityChange )
		self.Field_delta.Bind( wx.EVT_TEXT, self.onDeltaChanged )
		self.Field_mu.Bind( wx.EVT_TEXT, self.onmuChanged )
		self.Button_Save.Bind( wx.EVT_BUTTON, self.onSave )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onEnergyChanged( self, event ):
		event.Skip()
	
	def onSSHChanged( self, event ):
		event.Skip()
	
	def onSSVChanged( self, event ):
		event.Skip()
	
	def ongChanged( self, event ):
		event.Skip()
	
	def onIChanged( self, event ):
		event.Skip()
	
	def ondpsfChanged( self, event ):
		event.Skip()
	
	def onRChanged( self, event ):
		event.Skip()
	
	def onR_0Changed( self, event ):
		event.Skip()
	
	def onCheckChanged( self, event ):
		event.Skip()
	
	def ondChanged( self, event ):
		event.Skip()
	
	def onNChanged( self, event ):
		event.Skip()
	
	def onroughnessChanged( self, event ):
		event.Skip()
	
	def onWChanged( self, event ):
		event.Skip()
	
	def onChangeMaterial( self, event ):
		event.Skip()
	
	def onDensityChange( self, event ):
		event.Skip()
	
	def onDeltaChanged( self, event ):
		event.Skip()
	
	def onmuChanged( self, event ):
		event.Skip()
	
	def onSave( self, event ):
		event.Skip()
	

