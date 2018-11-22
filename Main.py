import sys
import couchdb
import ctypes  # An included library with Python install.
from PyQt5 import uic, QtWidgets
import json
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget,QTableWidgetItem
from PyQt5 import QtGui
# -------------------------------------------------------------------------------

qtCreatorFile = "GUI.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Conexion a la BASE DE DATOS
couch = couchdb.Server("http://127.0.0.1:5984")
db = couch['test2']
propietarios=[]
farmaceuticos=[]
productos=[]
almacenes=[]


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        ##############
        ##############AGREGAR
        ##############
        # Agregar Farmaceutico
        self.bt_Farmaceutico_agregar_2.clicked.connect(self.agregarFarmaceutico)
        # Agregar Propietarios
        self.bt_propietario_agregar.clicked.connect(self.agregarPropietario)
        # agregar Laboratorios
        self.bt_Laboratorio_agregar.clicked.connect(self.agregarLaboratorio)
        # Agregar Productos
        self.bt_Producto_agregar.clicked.connect(self.agregarProductos)
        # AgregarFarmacia
        self.bt_Farmacia_Agregar.clicked.connect(self.agregarFarmacia)
        ################
        ################  ELIMINAR
        ################
        # prueba eliminar
        self.bt_Producto_Eliminar.clicked.connect(self.delete)
        # eliminar Farmaceutico
        self.bt_Farmaceutico_Eliminar.clicked.connect(self.AccionEliminarFarmaceutico)
        # eliminar Propietario
        self.bt_propietario_Eliminar.clicked.connect(self.AccionEliminarPropietario)
        # eliminar Productos
        self.bt_Producto_Eliminar.clicked.connect(self.AccionEliminarProducto)
        # eliminar Laboratorio
        self.bt_Laboratorio_Eliminar.clicked.connect(self.AccionEliminarLaboratorio)
        # eliminar Farmacias
        self.bt_Farmacia_Eliminar.clicked.connect(self.AccionEliminarFarmacia)
        ################
        ################ ACTUALIZAR
        ################
        # Actualizar Farmaceutico
        self.bt_Farmaceutico_Modificar.clicked.connect(self.AccionModificarFarmaceutico)
        # Actualizar Propietario
        self.bt_propietario_Modificar.clicked.connect(self.AccionModificarPropietario)
        # Actualizar Laboratorio
        self.bt_Laboratorio_Modificar.clicked.connect(self.AccionModificarLaboratorio)
        # Actualizar Producto
#        self.bt_Producto_Modificar.clicked(self.AccionModificarProducto)
        ################
        ################ BUSCAR
        ################
        self.bt_FindFarmacia.clicked.connect(self.BuscarFarmacia)
        self.bt_FindFarmaceutico.clicked.connect(self.BuscarFarmaceutico)
        self.bt_FindPropietario.clicked.connect(self.BuscarPropietaraio)
        self.bt_FindLaboratorio.clicked.connect(self.BuscarLaboratorio)
        self.bt_FindProducto.clicked.connect(self.BuscarProducto)
        ################
        ############### TAB BAR CLICKED
        ################
        self.bt_Farmacia_BuscarProductos.clicked.connect(self.AccionBuscarProductos)
        self.bt_load.clicked.connect(self.loadComboboxes)
        self.bt_Farmacia_asigPropietarios.clicked.connect(self.asignarPropietario)
        self.bt_Farmacia_asigFarmaceuticos.clicked.connect(self.asignarFarmaceuticos)
        self.bt_agregarAlmacen.clicked.connect(self.agregarAlmacen)
        self.bt_asignaralmancen.clicked.connect(self.asignarAlamacen)
        self.bt_loadprodlab.clicked.connect(self.loadPro)
        self.bt_Farmacia_BuscarProductos.clicked.connect(self.loadAlmacenesfar)
        self.bt_almacen_farmacia.clicked.connect(self.loadProductosfar)



    def AgregarProductoALAb(self):
        codigo = self.tf_Laboratorio_IdProduct.text()
        doc=db.get(codigo)
        cantidad = self.tf_Laboratorio_cantidadProduct.text()
        costoVenta = self.tf_Laboratorio_costoVentaProducto.text()
        nombre = self.doc.get('nombre')
        fabricante=self.doc.get('fabricante')
        precioCoste=self.doc.get('precioCoste')
        categoria = self.doc.get('categoria')
        descripcion = self.doc.get('descripcion')
        seguro = self.doc.get('seguro')
        arregloTemo= doc.get('array')
        arregloTemo.append(codigo)def AgregarProductoALAb(self):
        codigo = self.tf_Laboratorio_IdProduct.text()
        doc=db.get(codigo)
        cantidad = self.tf_Laboratorio_cantidadProduct.text()
        costoVenta = self.tf_Laboratorio_costoVentaProducto.text()
        nombre = self.doc.get('nombre')
        fabricante=self.doc.get('fabricante')
        precioCoste=self.doc.get('precioCoste')
        categoria = self.doc.get('categoria')
        descripcion = self.doc.get('descripcion')
        seguro = self.doc.get('seguro')

        arregloTemo= doc.get('array')
        arregloTemo.append(codigo)

    def loadProductosfar(self):
        doc=db.get(self.tf_alamacenfarma.text())
        array=doc.get('productos')
        print (array)
        print (array)
        self.tableWidget.setRowCount(len(array))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Codigo"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Nombre"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Cantidad"))
        i=0
        for e in doc:
            if(i<len(array)):
                self.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(array[i]))
                self.tableWidget.setItem(i,1, QtWidgets.QTableWidgetItem(db.get(array[i]).get('nombre')))
                self.tableWidget.setItem(i,2, QtWidgets.QTableWidgetItem(db.get(array[i]).get('cantidad')))
            else:
                break
            i=i+1

    def loadAlmacenesfar(self):

        doc=db.get(self.tf_Farmacia_CodFarmaciaAlmacenBuscar.text())
        array=doc.get('almacenes')
        print (array)
        self.tb_almacenesfarma.setRowCount(len(array))
        self.tb_almacenesfarma.setColumnCount(3)
        self.tb_almacenesfarma.setHorizontalHeaderItem(0, QTableWidgetItem("Codigo"))

        i=0
        for e in doc:
            if(i<len(array)):
                self.tb_almacenesfarma.setItem(i,0, QtWidgets.QTableWidgetItem(array[i]))
            else:
                break
            i=i+1





    def loadPro(self):
        torequest=requests.get('http://127.0.0.1:5984/test2/_design/list/_view/productos')
        doc=torequest.json().get('rows')

        self.tb_lab_agregarproducto.setRowCount(len(doc))
        self.tb_lab_agregarproducto.setColumnCount(3)
        self.tb_lab_agregarproducto.setHorizontalHeaderItem(0, QTableWidgetItem("Codigo"))
        self.tb_lab_agregarproducto.setHorizontalHeaderItem(1, QTableWidgetItem("Nombre"))
        self.tb_lab_agregarproducto.setHorizontalHeaderItem(2, QTableWidgetItem("Cantidad"))
        i=0
        for e in doc:
            self.tb_lab_agregarproducto.setItem(i,0, QtWidgets.QTableWidgetItem(e.get('key')))
            self.tb_lab_agregarproducto.setItem(i,1, QtWidgets.QTableWidgetItem(db.get(e.get('key')).get('nombre')))
            self.tb_lab_agregarproducto.setItem(i,2, QtWidgets.QTableWidgetItem(db.get(e.get('key')).get('cantidad')))
            i=i+1


    def agregarAlmacen(self):
        codigo= self.tf_codigo_almacenes.text()
        array=[]
        doc = {
            '_id': codigo,
            'productos':array,
            'tipo':'almacenes'
        }
        db.save(doc)
        self.tf_codigo_almacenes.setText("")
    def asignarAlamacen(self):
        almacenes.append(self.cb_almaneces.currentText())
        index=self.cb_almaneces.currentIndex()
        self.cb_almaneces.removeItem(index)
        self.bt_load.setEnabled(False)
        print (almacenes)

    def asignarPropietario(self):
        propietarios.append(self.cb_Farmacia_Propietarios.currentText())
        index=self.cb_Farmacia_Propietarios.currentIndex()
        self.cb_Farmacia_Propietarios.removeItem(index)
        self.bt_load.setEnabled(False)

    def asignarFarmaceuticos(self):
        farmaceuticos.append(self.cb_Farmacia_farmaceuticos.currentText())
        index=self.cb_Farmacia_farmaceuticos.currentIndex()
        self.cb_Farmacia_farmaceuticos.removeItem(index)
        self.bt_load.setEnabled(False)

    def AccionBuscarProductos(self):
        torequest=requests.get('http://127.0.0.1:5984/test2/_design/List_productos/_view/view_list_productos')
        doc=torequest.json().get('rows')



    def AccionModificarProducto(self):
        doc = db[self.tf_Producto_id.text()]
        db.delete(doc)
        id = self.tf_Producto_id.text()
        precioCosto=self.tf_Producto_precioCoste.text()
        precioVenta=self.tf_Producto_PrecioVenta.text()
        nombre = self.tf_Producto_nombre.text()
        fabricante = self.tf_Producto_Fabricante.text()
        seguro = self.cb_Producto_TieneProteccion.currentText()
        cantidad= self.tf_Producto_cantidad.text()
        categoria = self.tf_Producto_Categoria.text()
        descripcion = self.tf_Producto_DescripcionProducto.toPlainText()
        doc = {
            '_id': id,
            'nombre': nombre,
            'fabricante': fabricante,
            'precioCosto': precioCosto,
            'precioVenta': precioVenta,
            'cantidad': cantidad,
            'seguro': seguro,
            'categoria': categoria,
            'descripcion': descripcion,
            'tipo':"producto"

        }
        db.save(doc)
        id = self.tf_Producto_id.setText("")
        self.tf_Producto_nombre.setText("")
        self.tf_Producto_Fabricante.setText("")
        self.tf_Producto_precioCoste.setText("")
        self.tf_Producto_PrecioVenta.setText("")
        self.tf_Producto_Categoria.setText("")
        self.tf_Producto_DescripcionProducto.setPlainText("")

    def AccionModificarLaboratorio(self):
        doc = db[self.tf_Laboratorio_id.text()]
        db.delete(doc)
        id = self.tf_Laboratorio_id.text()
        nombre = self.tf_Laboratorio_nombre.text()
        doc = {
            '_id': id,
            'nombre': nombre,
            'tipo':'laboratorio'

        }
        db.save(doc)

    def AccionModificarFarmaceutico(self):
        doc = db[self.tf_Farmaceutico_id.text()]
        db.delete(doc)
        id = self.tf_Farmaceutico_id.text()
        nombre = self.tf_Farmaceutico_nombre.text()
        direccion = self.tf_Farmaceutico_direccion.text()
        edad = self.tf_Farmaceutico_edad.text()
        persona = ("Farmaceutico")
        doc = {
            '_id': id,
            'nombre': nombre,
            'direccion': direccion,
            'edad': edad,
            'tipo': persona
        }
        db.save(doc)

    def BuscarProducto(self):
       doc=db.get(self.tf_Producto_id.text())
       self.tf_Producto_nombre.setText(doc.get('nombre'))
       self.tf_Producto_Fabricante.setText(doc.get('fabricate'))
       self.tf_Producto_precioCoste.setText(doc.get('precioCosto'))
       self.tf_Producto_PrecioVenta.setText(doc.get('precioVenta'))
       self.tf_Producto_Categoria.setText(doc.get('categoria'))
       self.tf_Producto_Cantidad.setText(doc.get('cantidad'))
       self.tf_Producto_DescripcionProducto.setPlainText(doc.get('descripcion'))

    def BuscarLaboratorio(self):
        doc=db.get(self.tf_Laboratorio_id.text())
        self.tf_Laboratorio_nombre.setText(doc.get('nombre'))

    def BuscarPropietaraio(self):
        doc=db.get(self.tf_propietario_id.text())
        print(doc)
        self.tf_propietario_nombre.setText(doc.get('nombre'))
        self.tf_propietario_direccion.setText(doc.get('direccion'))
        self.tf_propietario_edad.setText(doc.get('edad'))

    def BuscarFarmaceutico(self):
        doc=db.get(self.tf_Farmaceutico_id.text())
        self.tf_Farmaceutico_nombre.setText(doc.get('nombre'))
        self.tf_Farmaceutico_direccion.setText(doc.get('direccion'))
        self.tf_Farmaceutico_edad.setText(doc.get('edad'))


    def BuscarFarmacia(self):
        doc=db.get(self.tf_Farmacia_codigoFarm.text())
        self.tf_Farmacia_Ciudad.setText(doc.get('ciudad'))
        self.tf_Farmacia_departamento.setText(doc.get('departamento'))
        self.tf_Farmacia_calle.setText(doc.get('calle'))

    def AccionModificarPropietario(self):
        doc = db[self.tf_propietario_id.text()]
        db.delete(doc)
        id = self.tf_propietario_id.text()
        nombre = self.tf_propietario_nombre.text()
        direccion = self.tf_propietario_direccion.text()
        edad = self.tf_propietario_edad.text()
        persona = ("Propietario")
        doc = {
            '_id': id,
            'nombre': nombre,
            'direccion': direccion,
            'edad': edad,
            'tipo': persona

        }
        db.save(doc)
        self.tf_propietario_id.setText("")
        self.tf_propietario_nombre.setText("")
        self.tf_propietario_direccion.setText("")
        self.tf_propietario_edad.setText("")

    def delete(self):
        doc = db['1322']
        db.delete(doc)

    def AccionEliminarFarmaceutico(self):
        doc = db[self.tf_Farmaceutico_id.text()]
        db.delete(doc)

    def AccionEliminarPropietario(self):
        doc = db[self.tf_propietario_id.text()]
        db.delete(doc)
        self.tf_propietario_id.setText("")
        self.tf_propietario_nombre.setText("")
        self.tf_propietario_direccion.setText("")
        self.tf_propietario_edad.setText("")

    def AccionEliminarProducto(self):
        doc = db[self.tf_Producto_id.text()]
        db.delete(doc)

    def AccionEliminarLaboratorio(self):
        doc = db[self.tf_Laboratorio_id.text()]
        db.delete(doc)

    def AccionEliminarFarmacia(self):
        doc = db[self.tf_Farmacia_codigoFarm.text()]
        db.delete(doc)

    def agregarFarmacia(self):
        cod = self.tf_Farmacia_codigoFarm.text()
        ciudad = self.tf_Farmacia_Ciudad.text()
        departamento = self.tf_Farmacia_departamento.text()
        calle = self.tf_Farmacia_calle.text()
        doc = {
            '_id': cod,
            "direccion":{ "ciudad": ciudad,
                         "departamento": departamento,
                         "calle":calle
                         },
            "almacenes":almacenes,
            "propietarios":propietarios,
            "farmaceuticos":farmaceuticos,
            "tipo":"farmacia"
        }
        db.save(doc)
        self.bt_load.setEnabled(True)

    def loadComboboxes(self):
        torequest=requests.get('http://127.0.0.1:5984/test2/_design/list/_view/propietarios')
        doc=torequest.json().get('rows')
        self.cb_Farmacia_Propietarios.clear()
        for e in doc:
            self.cb_Farmacia_Propietarios.addItem(e.get('key'))
        torequest=requests.get('http://127.0.0.1:5984/test2/_design/list/_view/farmaceuticos')
        doc=torequest.json().get('rows')
        self.cb_Farmacia_farmaceuticos.clear()
        for e in doc:
            self.cb_Farmacia_farmaceuticos.addItem(e.get('key'))
        torequest=requests.get('http://127.0.0.1:5984/test2/_design/list/_view/almacenes')
        doc=torequest.json().get('rows')
        self.cb_almaneces.clear()
        for e in doc:
            self.cb_almaneces.addItem(e.get('key'))



    def loadPropietarios(self):
        self.cb_Farmacia_Propietarios.clear()
        for e in propietarios:
            self.cb_Farmacia_Propietarios.addItem(e)

    def agregarProductos(self):
        id = self.tf_Producto_id.text()
        nombre = self.tf_Producto_nombre.text()
        fabricante = self.tf_Producto_Fabricante.text()
        seguro = self.cb_Producto_TieneProteccion.currentText()
        cantidad= self.tf_Producto_Cantidad.text()
        categoria = self.tf_Producto_Categoria.text()
        descripcion = self.tf_Producto_DescripcionProducto.toPlainText()
        doc = {
            '_id': id,
            'nombre': nombre,
            'fabricante': fabricante,
            'precioCosto': '',
            'precioVenta': '',
            'cantidad': cantidad,
            'seguro': seguro,
            'categoria': categoria,
            'descripcion': descripcion,
            'tipo':"producto"

        }
        db.save(doc)
        id = self.tf_Producto_id.setText("")
        self.tf_Producto_nombre.setText("")
        self.tf_Producto_Fabricante.setText("")
        self.tf_Producto_precioCoste.setText("")
        self.tf_Producto_PrecioVenta.setText("")
        self.tf_Producto_Categoria.setText("")
        self.tf_Producto_Cantidad.setText("")
        self.tf_Producto_DescripcionProducto.setPlainText("")

    def agregarLaboratorio(self):
        id = self.tf_Laboratorio_id.text()
        nombre = self.tf_Laboratorio_nombre.text()
        doc = {
            '_id': id,
            'nombre': nombre,
            'tipo':'laboratorio'

        }
        db.save(doc)
        self.tf_Laboratorio_id.setText("")
        self.tf_Laboratorio_nombre.setText("")

    def agregarPropietario(self):
        id = self.tf_propietario_id.text()
        nombre = self.tf_propietario_nombre.text()
        direccion = self.tf_propietario_direccion.text()
        edad = self.tf_propietario_edad.text()
        persona = ("Propietario")

        doc = {
            '_id': id,
            'nombre': nombre,
            'direccion': direccion,
            'edad': edad,
            'tipo': persona

        }
        db.save(doc)
        self.tf_propietario_id.setText("")
        self.tf_propietario_nombre.setText("")
        self.tf_propietario_direccion.setText("")
        self.tf_propietario_edad.setText("")

    def agregarFarmaceutico(self):
        id = self.tf_Farmaceutico_id_2.text()
        nombre = self.tf_Farmaceutico_nombre_2.text()
        direccion = self.tf_Farmaceutico_direccion_2.text()
        edad = self.tf_Farmaceutico_edad_2.text()
        persona = ("Farmaceutico")
        doc = {
            '_id': id,
            'nombre': nombre,
            'direccion': direccion,
            'edad': edad,
            'tipo': persona


        }
        db.save(doc)
        self.tf_Farmaceutico_id_2.setText("")
        self.tf_Farmaceutico_nombre_2.setText("")
        self.tf_Farmaceutico_direccion_2.setText("")
        self.tf_Farmaceutico_edad_2.setText("")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
