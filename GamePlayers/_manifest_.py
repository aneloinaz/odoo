{
    'name': 'Gestión de Biblioteca',
    'version': '1.0',
    'summary': 'Módulo para gestionar libros',
    'description': 'Permite registrar libros y autores',
    'author': 'Tu Nombre',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/libro_views.xml',
    ],
    'installable': True,
    'application': True,
}
