
import sys
import couchdb
#----------------------------DOCUMENTOS---------------------------------
from couchdb.mapping import Document, IntegerField, TextField,FloatField,DocumentMeta

class Farmaceutico(Document):
    item=TextField()
    id = IntegerField()
    nombre = TextField()
    direccion = TextField()
    edad =IntegerField()

class Propietario(Document):
    item=TextField()
    id = IntegerField()
    nombre = TextField()
    direccion = TextField()
    edad =IntegerField()

class Laboratorio(Document):
    item=TextField()
    id = IntegerField()
    nombre = TextField()

class Producto(Document):
    item=TextField()
    id=IntegerField()
    nombre=TextField()
    fabricante=TextField()
    precioCoste=FloatField()
    precioVenta=FloatField()
    seguro=TextField()
#----------------------------------------------------------------------------



#----------------------------------------------------------------------------

from PyQt5 import uic, QtWidgets

class Productos:
    id=IntegerField
    nombre=TextField
    fabricante=TextField
    precioCoste=FloatField
    precioVenta=FloatField
    seguro=TextField
    def __init__(self,id,nombre,fabricantw,precioc,preciov,seguro):
        self.id=id
        self.nombre=nombre
        self.fabricante=fabricantw
        self.precioCoste=precioc
        self.precioVenta=preciov
        self.seguro=seguro
    
        
qtCreatorFile = "GUI.ui" # Nombre del archivo aquí.
couch = couchdb.Server('http://127.0.0.1:5984')
dbname='test2'
db2 = couch[dbname]
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
from couchdb import Server
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

   def agregarProductos(self):
        id= self.tf_Producto_id.text()
        nombre=self.tf_Producto_nombre.text()
        fabricante =self.tf_Producto_Fabricante.text()
        precioCoste=self.tf_Producto_precioCoste.text()
        precioVenta=self.tf_Producto_PrecioVenta.text()
        seguro=self.cb_Producto_TieneProteccion.currentText()
        pro= Producto(item='Producto',
                      id=int(id),
                      nombre=nombre,
                      fabricante=fabricante,
                      precioCoste=float(precioCoste),
                      precioVenta=float(precioVenta),
                      seguro=seguro)
        pro.store(db2)
        produc = Producto.load(db2,32)
        print ("ID", produc.id," nombre:",produc.nombre)

   def agregarLaboratorio(self):
        id= self.tf_Laboratorio_id.text()
        nombre=self.tf_Laboratorio_nombre.text()
        lab= Laboratorio(item='Laboratorio',
                         id=int(id),
                         nombre=nombre)
        lab.store(db2)

   def agregarPropietario(self):
        id= self.tf_propietario_id.text()
        nombre=self.tf_propietario_nombre.text()
        direccion =self.tf_propietario_direccion.text()
        edad=self.tf_propietario_edad.text()
        prop = Propietario( item='Propietario',
                            id=int(id),
                            nombre=nombre,
                            direccion=direccion,
                            edad=int(edad))
        prop.store(db2)

   def agregarFarmaceutico(self):
        id= self.tf_Farmaceutico_id.text()
        nombre=self.tf_Farmaceutico_nombre.text()
        direccion =self.tf_Farmaceutico_direccion.text()
        edad=self.tf_Farmaceutico_edad.text()
        farma = Farmaceutico(item='Farmaceutico',
                            id=int(id),
                            nombre=nombre,
                            direccion=direccion,
                            edad=int(edad))

        farma.store(db2)


if __name__ == "__main__":
   app =  QtWidgets.QApplication(sys.argv)
   window = MyApp()
   window.show()
   sys.exit(app.exec_())





