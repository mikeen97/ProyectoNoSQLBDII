
import sys
import couchdb
from PyQt5 import uic, QtWidgets

#-------------------------------------------------------------------------------

qtCreatorFile = "GUI.ui" # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#Conexion a la BASE DE DATOS
couch = couchdb.Server("http://127.0.0.1:5984")
db  = couch['test2']

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):


   def __init__(self):
       QtWidgets.QMainWindow.__init__(self)
       Ui_MainWindow.__init__(self)
       self.setupUi(self)
       #Agregar Farmaceutico
       self.bt_Farmaceutico_agregar.clicked.connect(self.agregarFarmaceutico)
       #Agregar Propietarios
       self.bt_propietario_agregar.clicked.connect(self.agregarPropietario)
       #agregar Laboratorios
       self.bt_Laboratorio_agregar.clicked.connect(self.agregarLaboratorio)
       #Agregar Productos
       self.bt_Producto_agregar.clicked.connect(self.agregarProductos)
       #prueba eliminar
       self.bt_Producto_Eliminar.clicked.connect(self.delete)

   def delete(self):
        doc= db['1322']
        db.delete(doc)



   def agregarProductos(self):
        id= self.tf_Producto_id.text()
        nombre=self.tf_Producto_nombre.text()
        fabricante =self.tf_Producto_Fabricante.text()
        precioCoste=self.tf_Producto_precioCoste.text()
        precioVenta=self.tf_Producto_PrecioVenta.text()
        seguro=self.cb_Producto_TieneProteccion.currentText()
        categoria=self.tf_Producto_Categoria.text()
        descripcion=self.tf_Producto_DescripcionProducto.toPlainText()
        doc = {
            '_id': id,
            'content': {
                        'nombre': nombre,
                        'fabricante':fabricante,
                        'precioCosto': precioVenta,
                        'precioVenta':precioCoste,
                        'seguro': seguro,
                        'categoria':categoria,
                        'descripcion':descripcion
                        }
            }
        db.save(doc)


   def agregarLaboratorio(self):
        id= self.tf_Laboratorio_id.text()
        nombre=self.tf_Laboratorio_nombre.text()

   def agregarPropietario(self):
        id= self.tf_propietario_id.text()
        nombre=self.tf_propietario_nombre.text()
        direccion =self.tf_propietario_direccion.text()
        edad=self.tf_propietario_edad.text()


   def agregarFarmaceutico(self):
        id= self.tf_Farmaceutico_id.text()
        nombre=self.tf_Farmaceutico_nombre.text()
        direccion =self.tf_Farmaceutico_direccion.text()
        edad=self.tf_Farmaceutico_edad.text()



if __name__ == "__main__":
   app =  QtWidgets.QApplication(sys.argv)
   window = MyApp()
   window.show()
   sys.exit(app.exec_())





