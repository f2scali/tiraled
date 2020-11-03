# -*- coding: utf-8 -*-
'''
@Creador: Marco Antonio Castro
@Correo: soportesimplesoft@gmail.com
@fecha: 2020-11-01
@version:0.0.1a
'''
import wx
from FormTira import F2SDialNuevo
class ObjDlgNuevo():
    """docstring for DlgNuevo."""

    def __init__(self, padre, nombre, ruta, filas, columnas):
        self.ruta=ruta
        self.nombre=nombre
        self.filas=filas
        self.columnas=columnas
        self.obDialogo=F2SDialNuevo(padre)
        self.obDialogo.F2S_DnRuta.SetPath(ruta)
        self.obDialogo.F2S_DNombre.SetValue(nombre)
        self.obDialogo.F2S_Cols.SetValue(columnas)
        self.obDialogo.F2S_Filas.SetValue(filas)
        self.obDialogo.Bind(wx.EVT_BUTTON, self.onAceptar ,self.obDialogo.F2S_DNuevo)
        self.obDialogo.Bind(wx.EVT_BUTTON, self.onCancelar ,self.obDialogo.F2S_DbntCancelar)
        self.obDialogo.ShowModal()

    def onAceptar(self,evento):
        print ('Nuevo')
        self.ruta=self.obDialogo.F2S_DnRuta.GetPath()
        self.nombre=self.obDialogo.F2S_DNombre.GetValue()
        self.filas=int(self.obDialogo.F2S_Filas.GetValue())
        self.columnas=int(self.obDialogo.F2S_Cols.GetValue())
        self.obDialogo.Destroy()

    def onCancelar(self,evento):
        print ('Cancelar')
        self.obDialogo.Destroy()
