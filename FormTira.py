# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Nov  2 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class F2S_Pal
###########################################################################

class F2S_Pal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		F2S_Pal = wx.FlexGridSizer( 0, 2, 0, 0 )
		F2S_Pal.SetFlexibleDirection( wx.BOTH )
		F2S_Pal.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.F2S_ColorSelector = wx.ColourPickerCtrl( self.m_panel1, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer4.Add( self.F2S_ColorSelector, 0, wx.ALL|wx.EXPAND, 5 )

		self.F2S_ActivoColor = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.F2S_ActivoColor, 0, wx.ALL, 5 )

		self.F2S_Borrar = wx.Button( self.m_panel1, wx.ID_ANY, u"Limpiar", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.F2S_Borrar.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_WARNING, wx.ART_BUTTON ) )
		bSizer4.Add( self.F2S_Borrar, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer4 )
		self.m_panel1.Layout()
		bSizer4.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Color", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Fila", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.F2S_Filas = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.F2S_Filas, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Columnas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.F2S_Cols = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.F2S_Cols, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.F2S_BtnCambio = wx.Button( self.m_panel2, wx.ID_ANY, u"Cambiar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.F2S_BtnCambio, 0, wx.ALL, 5 )


		bSizer5.Add( fgSizer2, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Tamaño", False )

		bSizer7.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		F2S_Pal.Add( bSizer7, 0, wx.EXPAND, 5 )

		self.F2S_PanelGrilla = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.F2S_PanelGrilla.SetScrollRate( 5, 5 )
		self.F2S_PanelGrilla.SetMinSize( wx.Size( 720,760 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.F2S_Grilla = wx.grid.Grid( self.F2S_PanelGrilla, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.F2S_Grilla.CreateGrid( 16, 16 )
		self.F2S_Grilla.EnableEditing( True )
		self.F2S_Grilla.EnableGridLines( True )
		self.F2S_Grilla.EnableDragGridSize( False )
		self.F2S_Grilla.SetMargins( 0, 0 )

		# Columns
		self.F2S_Grilla.SetColSize( 0, 1 )
		self.F2S_Grilla.EnableDragColMove( False )
		self.F2S_Grilla.EnableDragColSize( True )
		self.F2S_Grilla.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.F2S_Grilla.SetRowSize( 0, 1 )
		self.F2S_Grilla.EnableDragRowSize( True )
		self.F2S_Grilla.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.F2S_Grilla.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.F2S_Grilla.SetMinSize( wx.Size( 680,680 ) )

		bSizer3.Add( self.F2S_Grilla, 1, wx.ALL|wx.EXPAND, 5 )


		self.F2S_PanelGrilla.SetSizer( bSizer3 )
		self.F2S_PanelGrilla.Layout()
		bSizer3.Fit( self.F2S_PanelGrilla )
		F2S_Pal.Add( self.F2S_PanelGrilla, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( F2S_Pal, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.F2S_StatusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem11 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Nuevo", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem11 )

		self.m_menuItem7 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Abrir", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem7 )

		self.m_menu1.AppendSeparator()

		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Guardar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menu1.AppendSeparator()

		self.m_menu11 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Led Arduino", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"PNG", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"JPG", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem4 )

		self.m_menuItem5 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"ICO", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem5 )

		self.m_menu1.AppendSubMenu( self.m_menu11, u"Exportar" )

		self.m_menu1.AppendSeparator()

		self.m_menuItem8 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem8 )

		self.m_menubar1.Append( self.m_menu1, u"Archivo" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.F2S_ColorSelector.Bind( wx.EVT_COLOURPICKER_CHANGED, self.On_CambioColor )
		self.F2S_Borrar.Bind( wx.EVT_BUTTON, self.onBorrar )
		self.F2S_BtnCambio.Bind( wx.EVT_BUTTON, self.OnCambioTam )
		self.F2S_Grilla.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.onSeleccionCelda )
		self.Bind( wx.EVT_MENU, self.onNuevo, id = self.m_menuItem11.GetId() )
		self.Bind( wx.EVT_MENU, self.onAbrir, id = self.m_menuItem7.GetId() )
		self.Bind( wx.EVT_MENU, self.onGuardar, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.onLedArduino, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.onGuardarPNG, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.OnExitApp, id = self.m_menuItem8.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def On_CambioColor( self, event ):
		event.Skip()

	def onBorrar( self, event ):
		event.Skip()

	def OnCambioTam( self, event ):
		event.Skip()

	def onSeleccionCelda( self, event ):
		event.Skip()

	def onNuevo( self, event ):
		event.Skip()

	def onAbrir( self, event ):
		event.Skip()

	def onGuardar( self, event ):
		event.Skip()

	def onLedArduino( self, event ):
		event.Skip()

	def onGuardarPNG( self, event ):
		event.Skip()

	def OnExitApp( self, event ):
		event.Skip()


###########################################################################
## Class F2SDialNuevo
###########################################################################

class F2SDialNuevo ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nueva Imagen", pos = wx.DefaultPosition, size = wx.Size( 300,249 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer7.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.F2S_DNombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.F2S_DNombre, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Ruta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer7.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.F2S_DnRuta = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer7.Add( self.F2S_DnRuta, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Fila", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.F2S_Filas = wx.TextCtrl( self, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.F2S_Filas, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Columnas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.F2S_Cols = wx.TextCtrl( self, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.F2S_Cols, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer2, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.F2S_DbntCancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.F2S_DbntCancelar, 0, wx.ALL, 5 )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.F2S_DNuevo = wx.Button( self, wx.ID_ANY, u"Nuevo..", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.F2S_DNuevo, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


