# -*- coding: utf-8 -*-
'''
@Creador: Marco Antonio Castro
@Correo: soportesimplesoft@gmail.com
@fecha: 2020-11-01
@version:0.0.1a

Futuro:
Herramientas
copiar, pegar, cortar.
regresar comandos, avanzar comando.

'''
import pathlib
from  os import path
from PIL import Image
import numpy as np
import wx
from FormTira import F2S_Pal
from DialNuevo import ObjDlgNuevo

class IncioInterface(F2S_Pal):

    def __init__(self, parent):
        F2S_Pal.__init__(self, parent)
        filas=16
        columnas=16
        self.nombre='nuevo'
        self.ruta=f'{pathlib.Path().absolute()}'
        self.TextoCol(0,columnas)
        self.F2S_Grilla.SetRowLabelValue(0, '000')
        self.F2S_Grilla.SetRowSize(0,40)
        self.F2S_Grilla.SetRowLabelSize(40)
        self.F2S_StatusBar.SetStatusText(f'ruta:{path.join(self.ruta,self.nombre)}.f2s')
        self.Abrir('f2slogo.npy')


    def onNuevo(self,evento):
        dialogo=ObjDlgNuevo(self, self.nombre, self.ruta, self.F2S_Filas.GetValue(),self.F2S_Cols.GetValue() )
        self.nombre = dialogo.nombre
        self.ruta = dialogo.ruta
        self.CambiarTamGrilla(dialogo.filas, dialogo.columnas)
        self.F2S_StatusBar.SetStatusText(f'ruta:{path.join(self.ruta,self.nombre)}.f2s')

    def OnExitApp(self, evento):
        self.Destroy()

    def onSeleccionCelda(self,evento):
        if self.F2S_ActivoColor.GetValue():
            print (evento.Col)
            print (evento.Row)
            color = self.F2S_ColorSelector.GetColour()
            self.F2S_Grilla.SetCellBackgroundColour(evento.Row,evento.Col, color)

    def onGuardar(self, evento):
        print ('Guardar')
        datos = np.zeros(( self.F2S_Grilla.GetNumberCols(),self.F2S_Grilla.GetNumberRows(), 3), dtype=np.uint8)
        print (datos)
        #COLORES
        for fila in range(0,self.F2S_Grilla.GetNumberRows()):
            for columna in range(0,self.F2S_Grilla.GetNumberCols()):
                celda =list(self.F2S_Grilla.GetCellBackgroundColour(fila,columna))
                datos[fila][columna]=celda[0:3]
        #CONTENIDO FALTA
        ruta=path.join(self.ruta,self.nombre)
        np.save(ruta,datos)
        wx.MessageBox(f'Archivo Guardado:\n{ruta}', 'Guardar doc.', wx.ICON_INFORMATION)


    def Abrir(self, archivo):
        print ('aqui')
        #Falta Verificar nombre Archivo
        # try:
        #     with open(pathname, 'r') as file:
        #         self.doLoadDataOrWhatever(file)
        # except IOError:
        #     wx.LogError("Cannot open file '%s'." % newfile)


        datos =np.load(archivo)
        filas=len(datos)
        columnas=len(datos[0])
        self.CambiarTamGrilla(filas, columnas)
        filas=0
        for arr_fila in datos:
            columnas=0
            for arr_columna in arr_fila:
                print ( filas, columnas, arr_columna)
                self.F2S_Grilla.SetCellBackgroundColour(filas, columnas, arr_columna)
                columnas +=1
            filas +=1
        self.F2S_Grilla.ForceRefresh()


    def onAbrir(self, evento):
        #Falta verificar si no se ha guardado la imagen
        # if self.contentNotSaved:
        #     if wx.MessageBox("Current content has not been saved! Proceed?", "Please confirm",
        #                      wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
        #         return

        with wx.FileDialog(self, "Abrir Imagen..", wildcard="Archivos npy  (*.npy)|*.npy",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:    return
            ruta = fileDialog.GetPath()
            self.Abrir (ruta )

    def onBorrar(self,evento):
        for fila in range( 0,self.F2S_Grilla.GetNumberRows() ):
            for columna in range( 0,self.F2S_Grilla.GetNumberCols() ):
                self.F2S_Grilla.SetCellBackgroundColour(fila, columna, (255,255,255))
        self.F2S_Grilla.ForceRefresh()

    def OnCambioTam(self,evento):
        self.CambiarTamGrilla(self.F2S_Filas.GetValue(),self.F2S_Cols.GetValue() )

    def CambiarTamGrilla(self, filas, columnas):
        try:
            filas=int(filas)
        except Exception as e:
            wx.MessageBox(f'Error en el valor de la filas\n{e}', 'Error', wx.ICON_ERROR)
            return
        try:
            columnas=int(columnas)
        except Exception as e:
            wx.MessageBox(f'Error en el valor de la Columnas\n{e}', 'Error', wx.ICON_ERROR)
            return

        actual = self.F2S_Grilla.GetNumberRows()
        print ('Ancho:',actual,' Filas:',filas)
        if actual < filas:
            self.F2S_Grilla.AppendRows(filas-actual)
        elif actual >filas:
            print (actual-filas)
            self.F2S_Grilla.DeleteRows(0,actual-filas)


        actual = self.F2S_Grilla.GetNumberCols()
        print ('Ancho:',actual,' Colunas:',columnas)
        if actual < columnas:
            self.F2S_Grilla.AppendCols(columnas-actual)
            self.TextoCol(actual,columnas)

        elif actual >columnas:
            print (actual-columnas)
            self.F2S_Grilla.DeleteCols(columnas, actual-columnas)
            self.TextoFilas(1,self.F2S_Grilla.GetNumberRows())

    def TextoCol(self, inicio, columnas):
        for col in range(inicio,columnas):
             self.F2S_Grilla.SetColSize( col, 40)
             self.F2S_Grilla.SetColLabelValue(col, f'{col}')

        self.TextoFilas(1,self.F2S_Grilla.GetNumberRows())

    def TextoFilas(self,inicio, filas):
        columnas = self.F2S_Grilla.GetNumberCols()
        for fila in range(inicio,filas):
            self.F2S_Grilla.SetRowSize(fila,40)
            self.F2S_Grilla.SetRowLabelValue(fila, '{:03d}'.format(fila * columnas))

    def onLedArduino(self,evento):
        nro_led=0
        ruta = path.join(self.ruta,self.nombre)
        salida=open(f'{ruta}.txt','w')
        for fila in range( 0,self.F2S_Grilla.GetNumberRows() ):
            for columna in range( 0,self.F2S_Grilla.GetNumberCols() ):
                 celda = self.F2S_Grilla.GetCellBackgroundColour(fila, columna)
                 salida.write (f'tira.setPixelColor({nro_led},{celda[0]},{celda[1]},{celda[2]});')
                 nro_led +=1
        salida.close()

    def onGuardarPNG(self,evento):
        datos = np.zeros(( self.F2S_Grilla.GetNumberCols(),self.F2S_Grilla.GetNumberRows(), 3), dtype=np.uint8)
        print (datos)
        #for fila in self.F2S_Grilla.GetNumberRows():
        for fila in range(0,self.F2S_Grilla.GetNumberRows()):
            for columna in range(0,self.F2S_Grilla.GetNumberCols()):
                celda =list(self.F2S_Grilla.GetCellBackgroundColour(fila,columna))
                datos[fila][columna]=celda[0:3]

        img = Image.fromarray(datos, 'RGB')
        ruta = path.join(self.ruta,self.nombre)
        img.save(f'{ruta}.png')

    def On_CambioColor(self,evento):
        color = self.F2S_ColorSelector.GetColour()
        #GetCellBackgroundColour(row, col)
        #llenar todo: self.F2S_Grilla.SetDefaultCellBackgroundColour(color)
        #print ('GetSelectedBlocks   : ',self.F2S_Grilla.GetSelectedBlocks())
        #print ('GetGridCursorCol    : ',self.F2S_Grilla.GetGridCursorCol())
        # print ('GetSelectedCols     : ', self.F2S_Grilla.GetSelectedCols())
        # print ('GetSelectedRows     : ',self.F2S_Grilla.GetSelectedRows())

        if self.F2S_Grilla.GetGridCursorCol() and self.F2S_Grilla.GetGridCursorRow():
            self.F2S_Grilla.SetCellBackgroundColour(self.F2S_Grilla.GetGridCursorRow(),
                                                    self.F2S_Grilla.GetGridCursorCol(), color)

        if len(self.F2S_Grilla.GetSelectedCols())>0:
            columnas=self.F2S_Grilla.GetSelectedCols()
            for fila in range( 0,self.F2S_Grilla.GetNumberRows() ):
                for columna in columnas:
                    self.F2S_Grilla.SetCellBackgroundColour(fila, columna, color)

        if len(self.F2S_Grilla.GetSelectedRows())>0:
            filas=self.F2S_Grilla.GetSelectedRows()
            for fila in filas:
                for columna in range( 0,self.F2S_Grilla.GetNumberCols() ):
                    self.F2S_Grilla.SetCellBackgroundColour(fila, columna, color)

        if self.F2S_Grilla.GetSelectedCells():
            seleccionadas=self.F2S_Grilla.GetSelectedCells()
            print('Celdas Seleccionadas:',seleccionadas )
            for celda in seleccionadas:
                if len(celda)>0:
                    self.F2S_Grilla.SetCellBackgroundColour(celda[0], celda[1], color)

        if self.F2S_Grilla.GetSelectionBlockTopLeft:
            print ('Bloque de Celdas')
            #print(self.F2S_Grilla.GetSelectionBlockTopLeft())
            #print(self.F2S_Grilla.GetSelectionBlockBottomRight())
            arriba=self.F2S_Grilla.GetSelectionBlockTopLeft()
            abajo =self.F2S_Grilla.GetSelectionBlockBottomRight()
            if len(arriba)>0 and len(abajo)>0:
                for fila in range (arriba[0][0], abajo[0][0] + 1):
                    for columna in range (arriba[0][1], abajo[0][1] + 1):
                        self.F2S_Grilla.SetCellBackgroundColour(fila, columna, color)


if __name__ == '__main__':
    aplicacion = wx.App()
    frame_usuario = IncioInterface(None)
    frame_usuario.Show()
    aplicacion.MainLoop()
