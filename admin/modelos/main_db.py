# -*- coding: utf-8 -*-
db=DB()
db('Cuentas').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db.load=True
db('Cuentas').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Cuentas').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Cuentas').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Cuentas').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Anuncios').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Portafolio').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Portafolio').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Portafolio').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Portafolio').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Portafolio').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('AdminMenu').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('AdminMenu').campo('Acción',db.str,False,True,False,False,0,-1,None,None)
db('AdminMenu').campo('Submenús',db.list,False,True,False,False,0,-1,None,None)
db('AdminMenu').campo('Icono',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Plugins').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Plugins').campo('Activo',db.bool,False,True,False,False,0,-1,None,None)
db('Plantillas').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Plantillas').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Plantillas').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Plantillas').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Plantillas').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Modelos').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Modelos').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Modelos').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Modelos').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Modelos').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Log').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Log').campo('Contenido',db.doc,False,True,False,False,0,-1,None,None)
db('Log').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Log').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Log').campo('Status',db.bool,False,True,False,False,0,-1,None,None)
db('Ayuda').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Ayuda').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Ayuda').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Ayuda').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Ayuda').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Editar tema').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Editar tema').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Editar tema').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Editar tema').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Editar tema').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Tema').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Tema').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Tema').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Tema').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Tema').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Configuración').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Tablas,args>Modelos').campo('Contenido',db.dict,False,True,False,False,0,-1,None,None)
db('args>Tablas').campo('Contenido',db.dict,False,True,False,False,0,-1,None,None)
db('Carpeta-privada').campo('cifrado',db.str,False,True,False,False,0,-1,None,None)
db('AdminMenu').insertar('Escritorio', None, [['Inicio', [None, {'titulo': 'Inicio', 'valor': 'Inicio'}, None]], ['Mi red', ['explorar', {'titulo': 'visitar sitio', 'valor': ['']}, None]], ['Visitar sitio', [None, {'titulo': 'visitar sitio', 'valor': ['../../woodridge']}, None]]], 'desktop.png')
db('AdminMenu').insertar('Entradas', 'listar', [['Todas las entradas', ['listar', {'titulo': 'P\xc3\xa1ginas', 'valor': 'Entradas'}, None]], ['A\xc3\xb1adir entrada', ['editar', {'titulo': 'A\xc3\xb1adir nueva P\xc3\xa1ginas', 'valor': ['Entrada', None]}, None]]], '001-symbol.png')
db('AdminMenu').insertar('P\xc3\xa1ginas', 'listar', [['Todos las p\xc3\xa1ginas', ['listar', {'titulo': 'P\xc3\xa1ginas', 'valor': 'Paginas'}, None]], ['A\xc3\xb1adir p\xc3\xa1gina', ['editar', {'titulo': 'A\xc3\xb1adir nueva P\xc3\xa1ginas', 'valor': ['Pagina', None]}, None]]], '001-symbol.png')
db('AdminMenu').insertar('Archivos', 'listar', [['Todos los archivos', ['listar', {'titulo': 'Archivos', 'valor': 'Archivos'}, None]], ['subir archivo', ['editar', {'titulo': 'Subir nuevo archivo', 'valor': ['Archivo', None]}, None]]], 'upload.png')
db('AdminMenu').insertar('Plantillas', 'listar', [['Todas las plantillas', ['listar', {'titulo': 'Plantillas', 'valor': 'Plantillas'}, None]], ['A\xc3\xb1adir plantilla', ['editar3', {'titulo': 'A\xc3\xb1adir nueva P\xc3\xa1ginas', 'valor': {'Plantilla': None}}, None]]], 'document-3.png')
db('AdminMenu').insertar('Dise\xc3\xb1os', 'listar', [['Todos los dise\xc3\xb1os ', ['editar2', {'titulo': 'Dise\xc3\xb1os', 'valor': {'Dise\xc3\xb1o': None}}, None]], ['A\xc3\xb1adir dise\xc3\xb1o', ['codear', {'titulo': 'A\xc3\xb1adir nuevo dise\xc3\xb1o', 'valor': {'Dise\xc3\xb1o': None}}, None]]], 'layers.png')
db('AdminMenu').insertar('Controladores', 'listar', [['Todos los controladores ', ['editar2', {'titulo': 'Controladores', 'valor': {'Controlador': None}}, None]], ['A\xc3\xb1adir controlador', ['codear', {'titulo': 'A\xc3\xb1adir nuevo controlador', 'valor': {'Controlador': None}}, None]]], 'layers.png')
db('AdminMenu').insertar('Modelos', 'listar', [['Todos los modelos ', ['editar2', {'titulo': 'Modelos', 'valor': {'Modelo': None}}, None]], ['A\xc3\xb1adir modelo', ['codear', {'titulo': 'A\xc3\xb1adir nuevo modelo', 'valor': {'Modelo': None}}, None]]], 'layers.png')
db('AdminMenu').insertar('Scripts', 'listar', [['Todos los Scripts ', ['editar2', {'titulo': 'Modelos', 'valor': {'Script': None}}, None]], ['A\xc3\xb1adir script', ['codear', {'titulo': 'A\xc3\xb1adir nuevo script', 'valor': {'Script': None}}, None]]], 'layers.png')
db('AdminMenu').insertar('Ajustes', 'listar', [['Ajustes ', ['editar2', {'titulo': 'Ajustes', 'valor': {'Ajustes': None}}, None]]], 'layers.png')
db('AdminMenu').insertar('Plugins', 'listar', [['Todos los Plugins', ['plugins', {'titulo': 'Plugins', 'valor': ''}, None]], ['Editar los Plugins', ['editar2', {'titulo': 'Plugins', 'valor': {'Plugin': None}}, None]]], 'layers.png')
db('AdminMenu').insertar('Gestion de usuarios', 'listar', [['Todos los usuarios', ['listar', {'titulo': 'Usuarios', 'valor': 'Usuarios'}, None]], ['Nuevo usuario', ['editar', {'titulo': 'Crear nuevo usuario', 'valor': ['Usuario', None]}, None]]], 'profile.png')
db('AdminMenu').insertar('Formularios', 'listar', [['Todos los formulario', ['listar', {'titulo': 'Formularios', 'valor': 'Formularios'}, None]], ['Entradas', ['post', {'titulo': 'Entradas', 'valor': 'Post-de-Formulario'}, None]], ['Nuevo formulario', ['editar', {'titulo': 'Crear nuevo formulario', 'valor': {'Formulario': None}}, None]]], 'list.png')
db('AdminMenu').insertar('Ayuda', 'listar', [['Todos los temas', ['listar', {'titulo': 'Ayuda', 'valor': 'Ayuda'}, None]], ['Editar tema de ayuda', ['post', {'titulo': 'Editar tema ', 'valor': 'Editar tema'}, None]], ['Nuevo tema de ayuda', ['editar', {'titulo': 'Nuevo tema de ayuda', 'valor': ['Ayuda', None]}, None]]], 'list.png')
db('Opciones').insertar('Booleano', ['', 'No', 'Yes'])
db('Editar tema').insertar('Rental Prospects 0', [{'Formulario': 'hidden-id', 'name': 'id', 'value': '0'}, [{'opcion': 0, 'Logo': 'img-admin', 'name': 'logo', 'value': 0}, {'Rental Prospects': 'text-admin', 'name': 'titulo', 'value': 'Rental Prospects'}, {'1- Name and Last Name': 'text', 'name': 'last_name', 'value': 'sdasd'}, {'2- Phone Number': 'text-phone', 'name': 'phone', 'value': 'asfas'}, {'3- Email Adress': 'text-email', 'name': 'email', 'value': 'jesus26abraham1996@gmail.com'}, {'opcion': 0, '4- Size of Apartment': 'select', 'value': 0, 'name': 'size_apartment'}, {'opcion': 0, '5- Does the person have a Section 8 Voucher or any other payment assistance?': 'select', 'name': 'voucher_payment', 'value': 0}, {'5.1-If so, of how much?': 'number', 'name': 'si_voucher_payment', 'value': 0}, {'descripcion': '# of Adults & # of Children (+ ages)', '7.-How many people will be living in the apartment?': 'text', 'name': 'live_pest', 'value': ''}, {'8.-Will you have pets living in the apartment?': 'number', 'name': 'pest_in_apartment', 'value': 2}, {'opcion': 0, 'name': 'any_evictions', 'value': 0, '9.-Have the person had any evictions?': 'select'}, {'opcion': 0, '10.- Do you have a criminal record': 'select', 'name': 'criminal_record', 'value': 0}, {'If so, when?': 'text', 'name': 'when', 'value': 'aafa'}, {'opcion': 0, 'name': 'what_type', 'value': 0, '11.- If so, what type?': 'select'}, {'Note': 'textarea', 'name': 'note', 'value': 'afafajf'}]], {'Post de Formulario': 0}, '19/7/2017 21:27:15', [])
db('args>Tablas').insertar({'Paginas': 'Paginas', 'Usuario': 'Usuarios', 'Galeria': 'Galerias', 'informaciones': 'Informaciones', 'Pagina': 'Paginas', 'ayuda': 'Ayuda', 'Entradas-de-ayuda': 'Entradas-de-ayuda', 'Archivos': 'Archivos', 'Formularios': 'Formularios', 'Informaciones': 'Informaciones', 'Entradas': 'Entradas', 'Post-de-Formulario': 'Post-de-Formulario', 'Ayuda': 'Ayuda'})
db('Tema').insertar('Clasico', [[{'opcion': 6, 'widget1': 'select', 'name': 'widget1', 'value': 0}, {'opcion': 6, 'widget2': 'select', 'name': 'widget2', 'value': 0}], [{'opcion': 6, 'Estilo': 'text', 'name': 'estilo', 'value': 0}]], {'tema': 0}, '12/7/2017 10:27:11', [])
db('Cuentas').insertar('Facebook', [[{'Red social': 'text', 'name': 'facebook', 'value': 'https://www.facebook.com'}]], {'Cuenta': 0}, '12/7/2017 10:27:11', [])
db('Cuentas').insertar('Twitter', [[{'Red social': 'text', 'name': 'twitter', 'value': 'https://www.twitter.com'}]], {'Cuenta': 1}, '12/7/2017 10:27:11', [])
db('Cuentas').insertar('Instagram', [[{'Red social': 'text', 'name': 'instagram', 'value': 'https://www.instagram.com'}]], {'Cuenta': 2}, '12/7/2017 10:27:11', [])
db('Plantillas').insertar('index', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'index'}, {'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-header', 'value': 'Home4'}, {'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 0}, {'opcion': 0, 'Slide 1': 'select', 'name': 'slide_1', 'value': 1}, {'opcion': 0, 'Slide 2': 'select', 'name': 'slide_2', 'value': 2}, {'opcion': 0, 'Slide 3': 'select', 'name': 'slide_3', 'value': 3}, {'opcion': 0, 'name': 'baner', 'value': 4, 'Fondo de baners': 'select'}], [{'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-about', 'value': 'About Us'}, {'Info Izq.': 'textarea', 'value': '<p><img class="width-100p" style="max-width: 500px;" src="apps/asosa/user/static/img/bg-feature.jpg" /></p>\r\n<div class="about">\r\n<h3 class="about__title font-roboto"><img class="height-3" src="apps/asosa/user/static/img/icon/icon1.png" />&nbsp;Building information</h3>\r\n<ul class="about__caracteristicas pad-l2">\r\n<li>14 buildings and 140 apartment.</li>\r\n<li>Laundry Room.</li>\r\n<li>Smoke detectors and Fire extinguishers.</li>\r\n<li>Parking.</li>\r\n<li>Marquis Rental Apartments accepts Section 8 vouchers.</li>\r\n</ul>\r\n</div>', 'name': 'info_izq'}, {'Info Der.': 'textarea', 'name': 'info_der', 'value': '<div class="property-info">\r\n<h2 class="font-roboto"><img class="height-5" src="apps/asosa/user/static/img/icon/icon3.png" />Property info</h2>\r\n<p>Marquis Rental Apartments is a garden-style community, centrally located in the heart of Tampa. We are only minutes away from Tampa International Airport, Tampa Stadium, Busch Gardens, Lowery Park, major shopping centers and the Downtown area. Marquis Rental Apartments is a perfect venue for families and seniors who wish to live in a quiet and friendly environment.</p>\r\n<p>Marquis Rental Apartments is a sophisticated community that combines casual and elegant living. With 140 apartments, our staff and residents maintain a solid reputation for being an excellent place to live. Marquis Rental Apartments had recently undergone major renovations including the revitalization of the building&rsquo;s exterior and landscaping, along with significant upgrades to many of the apartment units including new kitchens, vanities, HVAC systems and appliances.</p>\r\n</div>\r\n<div class="about">\r\n<h3 class="about__title font-roboto"><img class="height-3" src="apps/asosa/user/static/img/icon/icon2.png" />Location</h3>\r\n<p class="about__description">Marquis Rental Apartments is located on N Armenia Ave between Sligh and Hillsborough Ave, within walking distance to grocery and retail stores, banks, and recreational parks. The property has easy access to Public and School Bus Transportation near its front entrance. Located just 30 minutes from the crystal clear waters of the Gulf Beaches in St. Petersburg and Clearwater, Marquis Rental Apartments is the ideal community to raise a family or retire in elegant and affordable surroundings.</p>\r\n</div>'}], [{'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-floor-plans', 'value': 'Floor Plans'}, {'Titulo Izq.': 'text', 'name': 'titulo_izq', 'value': 'Virgo apartments'}, {'opcion': 0, 'Acci\xc3\xb3n Izq.': 'select', 'name': 'action_izq', 'value': 5}, {'opcion': 0, 'Imagen Izq miniatura': 'select', 'name': 'img_izq_min', 'value': 6}, {'Flash Izq.': 'textarea', 'name': 'flash_izq', 'value': '<h5><img src="apps/asosa/user/static/img/icon/004-sleeping-bed-silhouette.png" width="24" height="24" /><strong> Number of rooms:</strong> 1</h5>\r\n<h5><img src="apps/asosa/user/static/img/icon/003-toilet.png" width="24" height="24" /><strong> Number of bathrooms:</strong> 1</h5>\r\n<h5><img src="apps/asosa/user/static/img/icon/001-scale-screen.png" width="24" height="24" /><strong>Square Feet:</strong> 700</h5>\r\n<div class="text-center font-s30"><strong>&middot;&middot;&middot;</strong></div>'}, {'opcion': 0, 'Plano Izq.': 'select', 'name': 'plano_izq', 'value': 11}, {'Contenido Izq.': 'textarea', 'value': '<div class="text-left">\r\n<div class="pad-1 pad-t2 text-left d-inline-block  alg-top">\r\n<table style="height: auto; width: 368px; display: inline-block; vertical-align: top;">\r\n<tbody>\r\n<tr style="height: 39px; vertical-alig: top;">\r\n<td style="width: 186px; height: 39px; vertical-align: top;"><img src="apps/asosa/user/static/img/icon/004-sleeping-bed-silhouette.png" />&nbsp;<strong>Number of rooms:</strong>&nbsp;</td>\r\n<td style="width: 138px; height: 39px; vertical-align: top;">\r\n<p>&nbsp;1</p>\r\n</td>\r\n</tr>\r\n<tr style="height: 43px;">\r\n<td style="width: 186px; height: 43px; vertical-align: top;"><span style="font-size: 11pt;"><span style="font-size: 11pt;"><img src="apps/asosa/user/static/img/icon/003-toilet.png" />&nbsp;</span></span><span style="font-size: 11pt;"><strong>Number of bathrooms:</strong></span></td>\r\n<td style="width: 138px; height: 43px; vertical-align: top;">\r\n<p>&nbsp;1</p>\r\n</td>\r\n</tr>\r\n<tr style="height: 48px;">\r\n<td style="width: 186px; height: 48px; vertical-align: top;"><span style="font-size: 11pt;"><span style="font-size: 11pt;"><img src="apps/asosa/user/static/img/icon/001-scale-screen.png" />&nbsp;</span></span><span style="font-size: 11pt;"><strong>Square Feet:</strong></span></td>\r\n<td style="width: 138px; height: 48px; vertical-align: top;">\r\n<p>&nbsp;700</p>\r\n</td>\r\n</tr>\r\n<tr style="height: 39px;">\r\n<td style="width: 186px; height: 39px; vertical-align: top;"><span style="font-size: 11pt;"><span style="font-size: 11pt;"><img src="apps/asosa/user/static/img/icon/005-notes.png" />&nbsp;</span></span><span style="font-size: 11pt;"><strong>Price:</strong></span></td>\r\n<td style="width: 138px; height: 39px; vertical-align: top;">\r\n<p>&nbsp;$755 - $850</p>\r\n</td>\r\n</tr>\r\n<tr style="height: 46px;">\r\n<td style="width: 186px; height: 46px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/curriculum.png" />&nbsp;<strong>Application Fee:</strong></p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 46px; vertical-align: top;">&nbsp;$50 per adult (non refundable)</td>\r\n</tr>\r\n<tr style="height: 40px;">\r\n<td style="width: 186px; height: 40px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/012-customer-service.png" />&nbsp;<strong>Administration fee:</strong></p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 40px; vertical-align: top;">&nbsp;$100 (non refundable)</td>\r\n</tr>\r\n<tr style="height: 36px;">\r\n<td style="width: 186px; height: 36px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/011-locked.png" />&nbsp;<strong>Security Deposit:</strong></p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 36px; vertical-align: top;">&nbsp;$350+ (must qualify)</td>\r\n</tr>\r\n<tr style="height: 41px;">\r\n<td style="width: 186px; height: 41px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/010-transfer.png" />&nbsp;<strong>Transfer fee:</strong>&nbsp;</p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 41px; vertical-align: top;">$ 300 (non refundable)</td>\r\n</tr>\r\n<tr style="height: 36px;">\r\n<td style="width: 186px; height: 36px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/001-dog.png" />&nbsp;<strong>Pet fee:</strong></p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 36px; vertical-align: top;">&nbsp;$300 per pet (non refundable).</td>\r\n</tr>\r\n<tr style="height: 28px;">\r\n<td style="width: 186px; height: 28px; vertical-align: top;"><img style="font-size: 11pt; vertical-align: top;" src="apps/asosa/user/static/img/icon/002-drop.png" />&nbsp;<strong>Water NOT include</strong></td>\r\n<td style="width: 138px; height: 28px; vertical-align: top;">&nbsp;</td>\r\n</tr>\r\n</tbody>\r\n</table>\r\n</div>\r\n<div class="pad-1 pad-t2 text-left d-inline-block">\r\n<table style="height: auto; width: 310px; display: inline-block; vertical-align: top;">\r\n<tbody>\r\n<tr style="height: 40px;">\r\n<td style="width: 27px; height: 40px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/009-garbage.png" /></td>\r\n<td style="width: 269px; height: 40px; vertical-align: top;"><strong>Trash Include</strong></td>\r\n</tr>\r\n<tr style="height: 39px;">\r\n<td style="width: 27px; height: 39px; vertical-align: top;"><span style="font-size: 11pt;"><img src="apps/asosa/user/static/img/icon/003-pest-observation.png" /></span></td>\r\n<td style="width: 269px; height: 39px; vertical-align: top;">&nbsp;<strong>Pest Control</strong></td>\r\n</tr>\r\n<tr style="height: 46px;">\r\n<td style="width: 27px; height: 46px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/008-weekly-calendar.png" /></td>\r\n<td style="width: 269px; height: 46px; vertical-align: top;"><strong>7- 12 Month Leases</strong></td>\r\n</tr>\r\n<tr style="height: 36px;">\r\n<td style="width: 27px; height: 36px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/007-laundry-basket.png" /></td>\r\n<td style="width: 269px; height: 36px; vertical-align: top;"><strong>Laundry Room</strong></td>\r\n</tr>\r\n<tr style="height: 38px;">\r\n<td style="width: 27px; height: 38px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/006-step-ladder.png" /></td>\r\n<td style="width: 269px; height: 38px; vertical-align: top;"><strong>Swimming Pool</strong></td>\r\n</tr>\r\n<tr style="height: 36px;">\r\n<td style="width: 27px; height: 36px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/005-wardrobe.png" /></td>\r\n<td style="width: 269px; height: 36px; vertical-align: top;"><strong>Large Closets</strong></td>\r\n</tr>\r\n<tr style="height: 59px;">\r\n<td style="width: 27px; height: 59px; vertical-align: top;"><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/004-siren.png" /></td>\r\n<td style="width: 269px; height: 59px; vertical-align: top;"><strong>24 Hours Emergency Mantenience</strong></td>\r\n</tr>\r\n<tr style="height: 33px;">\r\n<td style="width: 27px; height: 33px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/001-animal-prints.png" /></td>\r\n<td style="width: 269px; height: 33px; vertical-align: top;"><strong>Pet Friendly</strong></td>\r\n</tr>\r\n<tr style="height: 27px;">\r\n<td style="width: 27px; height: 27px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/002-disco-ball.png" /></td>\r\n<td style="width: 269px; height: 27px; vertical-align: top;"><strong>Club House</strong></td>\r\n</tr>\r\n</tbody>\r\n</table>\r\n&nbsp;</div>\r\n</div>\r\n<div class="text-left"><strong>Apartment amenities</strong>\r\n<ul>\r\n<li>Full kitchen with refrigerator, stove, diswasher, garbage, disposal and cabinets</li>\r\n<li>Bathroom with tub, shower and vanity</li>\r\n<li>Walk-In closets</li>\r\n<li>Smoke detectors</li>\r\n</ul>\r\n</div>', 'name': 'content_izq'}, {'name': 'titulo_der', 'value': 'Floridian apartments', 'Titulo Der.': 'text'}, {'opcion': 0, 'Acci\xc3\xb3n Der.': 'select', 'name': 'action_der', 'value': 7}, {'opcion': 0, 'Imagen Der miniatura': 'select', 'name': 'img_der_min', 'value': 8}, {'Flash Der.': 'textarea', 'value': '<h5><img src="apps/asosa/user/static/img/icon/004-sleeping-bed-silhouette.png" width="24" height="24" /><strong> Number of rooms:</strong> 2</h5>\r\n<h5><img src="apps/asosa/user/static/img/icon/003-toilet.png" width="24" height="24" /><strong> Number of bathrooms:</strong> 1 and 1/2</h5>\r\n<h5><img src="apps/asosa/user/static/img/icon/001-scale-screen.png" width="24" height="24" /><strong> Square Feet:</strong> 980</h5>\r\n<div class="text-center font-s30"><strong>&middot;&middot;&middot;</strong></div>', 'name': 'flash_der'}, {'opcion': 0, 'Plano Der.': 'select', 'name': 'plano_der', 'value': 10}, {'Contenido Der.': 'textarea', 'name': 'content_der', 'value': '<div class="text-left">\r\n<div class="pad-1 pad-t2 text-left d-inline-block  alg-top">\r\n<table style="height: auto; width: 368px; display: inline-block; vertical-align: top;">\r\n<tbody>\r\n<tr style="height: 39px; vertical-alig: top;">\r\n<td style="width: 186px; height: 39px; vertical-align: top;"><img src="apps/asosa/user/static/img/icon/004-sleeping-bed-silhouette.png" />&nbsp;<strong>Number of rooms:</strong>&nbsp;</td>\r\n<td style="width: 138px; height: 39px; vertical-align: top;">\r\n<p>2</p>\r\n</td>\r\n</tr>\r\n<tr style="height: 43px;">\r\n<td style="width: 186px; height: 43px; vertical-align: top;"><span style="font-size: 11pt;"><span style="font-size: 11pt;"><img src="apps/asosa/user/static/img/icon/003-toilet.png" />&nbsp;</span></span><span style="font-size: 11pt;"><strong>Number of bathrooms:</strong></span></td>\r\n<td style="width: 138px; height: 43px; vertical-align: top;">\r\n<p>&nbsp;1 and 1/2</p>\r\n</td>\r\n</tr>\r\n<tr style="height: 48px;">\r\n<td style="width: 186px; height: 48px; vertical-align: top;"><span style="font-size: 11pt;"><span style="font-size: 11pt;"><img src="apps/asosa/user/static/img/icon/001-scale-screen.png" />&nbsp;</span></span><span style="font-size: 11pt;"><strong>Square Feet:</strong></span></td>\r\n<td style="width: 138px; height: 48px; vertical-align: top;">\r\n<p>&nbsp;980</p>\r\n</td>\r\n</tr>\r\n<tr style="height: 39px;">\r\n<td style="width: 186px; height: 39px; vertical-align: top;"><span style="font-size: 11pt;"><span style="font-size: 11pt;"><img src="apps/asosa/user/static/img/icon/005-notes.png" />&nbsp;</span></span><span style="font-size: 11pt;"><strong>Price:</strong></span></td>\r\n<td style="width: 138px; height: 39px; vertical-align: top;">\r\n<p>&nbsp;$875 - $950</p>\r\n</td>\r\n</tr>\r\n<tr style="height: 46px;">\r\n<td style="width: 186px; height: 46px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/curriculum.png" />&nbsp;<strong>Application Fee:</strong></p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 46px; vertical-align: top;">&nbsp;$50 per adult (non refundable)</td>\r\n</tr>\r\n<tr style="height: 40px;">\r\n<td style="width: 186px; height: 40px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/012-customer-service.png" />&nbsp;<strong>Administration fee:</strong></p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 40px; vertical-align: top;">&nbsp;$100 (non refundable)</td>\r\n</tr>\r\n<tr style="height: 36px;">\r\n<td style="width: 186px; height: 36px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/011-locked.png" />&nbsp;<strong>Security Deposit:</strong></p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 36px; vertical-align: top;">&nbsp;$350+ (must qualify)</td>\r\n</tr>\r\n<tr style="height: 41px;">\r\n<td style="width: 186px; height: 41px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/010-transfer.png" />&nbsp;<strong>Transfer fee:</strong>&nbsp;</p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 41px; vertical-align: top;">$ 300 (non refundable)</td>\r\n</tr>\r\n<tr style="height: 36px;">\r\n<td style="width: 186px; height: 36px; vertical-align: top;">\r\n<p><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/001-dog.png" />&nbsp;<strong>Pet fee:</strong></p>\r\n<p>&nbsp;</p>\r\n</td>\r\n<td style="width: 138px; height: 36px; vertical-align: top;">&nbsp;$300 per pet (non refundable).</td>\r\n</tr>\r\n<tr style="height: 28px;">\r\n<td style="width: 186px; height: 28px; vertical-align: top;"><img style="font-size: 11pt; vertical-align: top;" src="apps/asosa/user/static/img/icon/002-drop.png" />&nbsp;<strong>Water NOT include</strong></td>\r\n<td style="width: 138px; height: 28px; vertical-align: top;">&nbsp;</td>\r\n</tr>\r\n</tbody>\r\n</table>\r\n</div>\r\n<div class="pad-1 pad-t2 text-left d-inline-block">\r\n<table style="height: auto; width: 310px; display: inline-block; vertical-align: top;">\r\n<tbody>\r\n<tr style="height: 40px;">\r\n<td style="width: 27px; height: 40px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/009-garbage.png" /></td>\r\n<td style="width: 269px; height: 40px; vertical-align: top;"><strong>Trash Include</strong></td>\r\n</tr>\r\n<tr style="height: 39px;">\r\n<td style="width: 27px; height: 39px; vertical-align: top;"><span style="font-size: 11pt;"><img src="apps/asosa/user/static/img/icon/003-pest-observation.png" /></span></td>\r\n<td style="width: 269px; height: 39px; vertical-align: top;">&nbsp;<strong>Pest Control</strong></td>\r\n</tr>\r\n<tr style="height: 46px;">\r\n<td style="width: 27px; height: 46px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/008-weekly-calendar.png" /></td>\r\n<td style="width: 269px; height: 46px; vertical-align: top;"><strong>7- 12 Month Leases</strong></td>\r\n</tr>\r\n<tr style="height: 36px;">\r\n<td style="width: 27px; height: 36px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/007-laundry-basket.png" /></td>\r\n<td style="width: 269px; height: 36px; vertical-align: top;"><strong>Laundry Room</strong></td>\r\n</tr>\r\n<tr style="height: 38px;">\r\n<td style="width: 27px; height: 38px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/006-step-ladder.png" /></td>\r\n<td style="width: 269px; height: 38px; vertical-align: top;"><strong>Swimming Pool</strong></td>\r\n</tr>\r\n<tr style="height: 36px;">\r\n<td style="width: 27px; height: 36px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/005-wardrobe.png" /></td>\r\n<td style="width: 269px; height: 36px; vertical-align: top;"><strong>Large Closets</strong></td>\r\n</tr>\r\n<tr style="height: 59px;">\r\n<td style="width: 27px; height: 59px; vertical-align: top;"><img style="font-size: 14.6667px;" src="apps/asosa/user/static/img/icon/004-siren.png" /></td>\r\n<td style="width: 269px; height: 59px; vertical-align: top;"><strong>24 Hours Emergency Mantenience</strong></td>\r\n</tr>\r\n<tr style="height: 33px;">\r\n<td style="width: 27px; height: 33px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/001-animal-prints.png" /></td>\r\n<td style="width: 269px; height: 33px; vertical-align: top;"><strong>Pet Friendly</strong></td>\r\n</tr>\r\n<tr style="height: 27px;">\r\n<td style="width: 27px; height: 27px; vertical-align: top;"><img style="font-size: 11pt;" src="apps/asosa/user/static/img/icon/002-disco-ball.png" /></td>\r\n<td style="width: 269px; height: 27px; vertical-align: top;"><strong>Club House</strong></td>\r\n</tr>\r\n</tbody>\r\n</table>\r\n&nbsp;</div>\r\n</div>\r\n<div class="text-left"><strong>Apartment amenities</strong>\r\n<ul>\r\n<li>Full kitchen with refrigerator, stove, diswasher, garbage, disposal and cabinets</li>\r\n<li>Bathroom with tub, shower and vanity</li>\r\n<li>Walk-In closets</li>\r\n<li>Smoke detectors</li>\r\n</ul>\r\n</div>'}, {'opcion': 0, 'Fondo de la secci\xc3\xb3n': 'select', 'value': 9, 'name': 'fondo_floor'}], [{'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-gallery', 'value': 'Gallery'}, {'Video': 'text', 'name': 'video', 'value': 'https://www.youtube.com/embed/5ukjvBkjyWU'}, {'opcion': 0, 'Foto 1': 'select', 'name': 'foto_1', 'value': 12}, {'opcion': 0, 'Foto 2': 'select', 'name': 'foto_2', 'value': 13}, {'opcion': 0, 'Foto 3': 'select', 'name': 'foto_3', 'value': 14}, {'opcion': 0, 'Foto 4': 'select', 'name': 'foto_4', 'value': 15}, {'opcion': 0, 'Foto 5': 'select', 'value': 16, 'name': 'foto_5'}, {'opcion': 0, 'Foto 6': 'select', 'name': 'foto_6', 'value': 17}, {'opcion': 0, 'name': 'foto_7', 'value': 18, 'Foto 7': 'select'}, {'Foto 8': 'select', 'opcion': 0, 'name': 'foto_8', 'value': 19}, {'opcion': 0, 'Foto 9': 'select', 'name': 'foto_9', 'value': 20}, {'opcion': 0, 'Foto 10': 'select', 'name': 'foto_10', 'value': 21}, {'opcion': 0, 'Foto 11': 'select', 'name': 'foto_11', 'value': 22}, {'Foto 12': 'select', 'opcion': 0, 'name': 'foto_12', 'value': 23}], [{'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-more-options', 'value': 'More Options'}, {'opcion': 0, 'name': 'fondo_options', 'value': 24, 'Fondo': 'select'}, {'opcion': 0, 'name': 'option_1', 'value': 28, 'Opcion 1': 'select'}, {'Opcion 1 link': 'text', 'name': 'option_1_link', 'value': ''}, {'opcion': 0, 'Opcion 2': 'select', 'name': 'option_2', 'value': 27}, {'Opcion 2 link': 'text', 'name': 'option_2_link', 'value': 'http://www.royaltycourtapartments.com/'}, {'opcion': 0, 'Opcion 3': 'select', 'value': 31, 'name': 'option_3'}, {'Opcion 3 link': 'text', 'name': 'option_3_link', 'value': 'http://www.woodridgeatcarrollwood.com/home.html'}, {'opcion': 0, 'Opcion 4': 'select', 'name': 'option_4', 'value': 32}, {'Opcion 4 link': 'text', 'name': 'option_4_link', 'value': ''}], [{'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-contact-us', 'value': 'Contact Us'}, {'opcion': 0, 'Fondo de la Secci\xc3\xb3n': 'select', 'value': 33, 'name': 'fondo-contact-us'}, {'Mapa': 'text', 'name': 'mapa', 'value': 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d777.4741271780646!2d-82.485807!3d28.002626!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88c2c15799a89d49:0x73d861fd5711579a!2s2609+Gemini+Ct,+Tampa,+FL+33614!5e1!3m2!1ses-419!2sus!4v1487952654962'}, {'Info de contacto': 'textarea', 'name': 'info_contacto', 'value': '<div class="col-lg-6 col-xs-12"><img class="height-10 height-5-xs height-8-sm" src="apps/asosa/admin/static/archivos/Imagenes/Logo-Marquis--Blanco.png" alt="qrmarquis" />\r\n<div class="info white">\r\n<h2>Marquis Rentals apartments</h2>\r\n<p>2609 Gemini Court Tampa, Florida 33614</p>\r\n<p>Office (813) 879 - 5491</p>\r\n<p>Fax (813) 879 - 5492</p>\r\n<a href="mailto:office@marquisrentalapartments.com">office@marquisrentalapartments.com</a></div>\r\n</div>\r\n<div class="col-lg-4"><a class="btn white bg-bluelight font-roboto" style="background: linear-gradient(to bottom, rgba(147,206,222,1) 0%, rgba(117,189,209,1) 41%, rgba(73,165,191,1) 100%); filter: progid:DXImageTransform.Microsoft.gradient( startColorstr=\'#93cede\', endColorstr=\'#49a5bf\', GradientType=0 );" href="app=asosa&amp;vista=formulario"><strong>SUBMIT</strong></a> <img class="housing height-8 pad-l2" src="apps/asosa/user/static/img/EQUAL-HOUSING-FINAL2.png" alt="qrmarquis" /></div>'}, {'Cuenta Paypal': 'text', 'name': 'paypal', 'value': ''}]], {'Plantilla': 0}, '12/7/2017 10:27:11', ['Publicada'])
db('Plantillas').insertar('Rental Prospects', [[{'opcion': 0, 'Logo': 'img-admin', 'name': 'logo', 'value': 0}, {'Rental Prospects': 'text-admin', 'name': 'titulo', 'value': 'Rental Prospects'}, {'1- Name and Last Name': 'text', 'name': 'last_name', 'value': ''}, {'2- Phone Number': 'text-phone', 'name': 'phone', 'value': ''}, {'3- Email Adress': 'text-email', 'name': 'email', 'value': ''}, {'opcion': 8, '4- Size of Apartment': 'select', 'value': 0, 'name': 'size_apartment'}, {'opcion': 0, '5- Does the person have a Section 8 Voucher or any other payment assistance?': 'select', 'value': 0, 'name': 'voucher_payment', 'opciones': 'main'}, {'5.1-If so, of how much?': 'number', 'name': 'si_voucher_payment', 'value': 0}, {'descripcion': '# of Adults & # of Children (+ ages)', '7.-How many people will be living in the apartment?': 'text', 'name': 'live_pest', 'value': ''}, {'8.-Will you have pets living in the apartment?': 'number', 'name': 'pest_in_apartment', 'value': 0}, {'opcion': 6, 'name': 'any_evictions', 'value': 0, '9.-Have the person had any evictions?': 'select'}, {'If so, when?': 'text', 'name': 'when', 'value': ''}, {'opcion': 7, 'name': 'what_type', 'value': '', '11.- If so, what type?': 'select'}, {'Note': 'textarea', 'name': 'note', 'value': ''}]], {'Plantilla': 1}, '12/7/2017 10:27:11', ['Publicada'])
db('Configuración').insertar([[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'Jesus26abraham1996@gmail.com'}, {'Sitio web': 'text', 'name': 'web', 'value': 'zerpatechnology.com.ve'}], [{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'web', 'value': ['occoasolutions.com', 'iokary.com']}]])
db('Plugins').insertar('pageCreator', False)
db('Plugins').insertar('sc', True)
db('Plugins').insertar('miplugin', False)
db('Plugins').insertar('Estudiantes', False)
db('Tablas,args>Modelos').insertar({'Paginas': 'paginas', 'Usuarios': 'usuarios', 'Entradas-de-ayuda': 'ayuda', 'Usuario': 'usuarios', 'Publicaciones': 'publicaciones', 'Archivos': 'archivos', 'Formularios': 'formularios', 'Informaciones': 'informaciones', 'Entradas': 'paginas', 'Pagina': 'paginas', 'Entrada': 'paginas', 'Archivo': 'archivos', 'Post-de-Formulario': 'formularios', 'Galerias': 'galerias', 'Ayuda': 'ayuda', 'Plantillas': 'main'})
db('Ayuda').insertar('Primeros pasos', [[{'Titulo': 'titulo', 'name': 'titulo', 'value': 'Primeros pasos'}, {'Pagina': 'text-titulo', 'name': 'section-pag1', 'value': 'Primeros pasos'}, {'Contenido': 'textarea', 'name': 'pag1', 'value': ''}], [{'Titulo': 'titulo', 'name': 'titulo', 'value': 'Primeros pasos'}, {'Pagina': 'text-titulo', 'name': 'section-pag2', 'value': ''}, {'Contenido': 'textarea', 'name': 'pag2', 'value': ''}], [{'Titulo': 'titulo', 'name': 'titulo', 'value': 'Primeros pasos'}, {'Pagina': 'text-titulo', 'name': 'section-pag3', 'value': 'Primeros pasos'}, {'Contenido': 'textarea', 'name': 'pag3', 'value': ''}], [{'Titulo': 'titulo', 'name': 'titulo', 'value': 'Primeros pasos'}, {'Pagina': 'text-titulo', 'name': 'section-pag4', 'value': 'Primeros pasos'}, {'Contenido': 'textarea', 'name': 'pag4', 'value': ''}]], {'Ayuda': 0}, '12/7/2017 10:27:11', ['Publicada'])
db('AdminMenu').insertar('Manejador de AsenZor', 'listar', [['Webapps', ['allapps', {'titulo': 'Todos las aplicaciones', 'valor': 'Todos las aplicaciones'}, None]], ['Temas', ['allapps', {'titulo': 'Todos los temas ', 'valor': 'temas'}, None]], ['Nuevo tema ', ['editar', {'titulo': 'Nuevo tema', 'valor': ['tema', None]}, None]], ['Menus', ['menus', {'titulo': 'Menus ', 'valor': 'Menus'}, None]], ['Nuevo menu', ['editar', {'titulo': 'Menu ', 'valor': ['menu', None]}, None]], ['Actualizar', ['update', {'titulo': 'Actualizar ', 'valor': 'Actualizar'}, None]]], 'list.png')
db('AdminMenu').insertar('ShortCodes', 'listar', [['Todos los shortcodes', ['listar', {'titulo': 'Estudiantes', 'valor': ['Plugin', 'sc', 'Shortcodes']}, None]], ['crear shortcode', ['editar', {'titulo': 'Nuevo Shortcode', 'valor': ['Plugin', 'sc', 'Shortcode', None]}, None]], ['Galerias', ['listar', {'titulo': 'Nuevo Shortcode', 'valor': ['Plugin', 'sc', 'Galerias']}, None]], ['crear galeria', ['editar', {'titulo': 'Nuevo Shortcode', 'valor': ['Plugin', 'sc', 'Galeria', None]}, None]], ['Sliders', ['listar', {'titulo': 'Nuevo Shortcode', 'valor': ['Plugin', 'sc', 'Sliders']}, None]], ['crear slider', ['editar', {'titulo': 'Nuevo Shortcode', 'valor': ['Plugin', 'sc', 'Slider', None]}, None]]], '001-symbol.png')
db('Plugins').insertar('Portafolio', True)
db.load=True
db('AdminMenu').insertar('Portafolio', 'listar', [['Todas las paginas', ['listar', {'titulo': 'Paginas', 'valor': ['Plugin', 'Portafolio', 'Shortcodes']}, None]], ['crear pagina', ['editar', {'titulo': 'Nueva pagina', 'valor': ['Plugin', 'Portafolio', 'Shortcode', None]}, None]]], '001-symbol.png')
db('Plugins').insertar('Productos', True)
db.load=False
