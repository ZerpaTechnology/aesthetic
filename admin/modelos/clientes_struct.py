db=DB()
db('Clientes').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Clientes').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Clientes').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Clientes').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Clientes').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Clientes').insertar('ZBot', [[{'Nombre': 'text', 'name': 'nombre', 'value': 'ZBot'}, {'Email': 'text', 'value': 'zerpatechnology@gmail.com', 'name': 'email'}, {'Contenido': 'textarea', 'name': 'contenido', 'value': 'Hola como estas yo soy un Bot de prueba de un mensaje de contacto de un cliente'}]], {'Cliente': 0}, '12/7/2017 10:27:11', [])