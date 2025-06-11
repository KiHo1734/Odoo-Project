{
    'name': "Custom HR Module",
    'version': "1.0",  
    'depends': [
        'base',
        'base_setup',
    ],
    'author': "My Name",
    'category': "Customizations",
    'description': "Module description",
    'data': [
        'views/employee_detail_sequence.xml',
        'views/hr_form_view.xml',
        'views/custom_hr_menu.xml',
    ],
    'application': True,
    'installable': True, 
    'auto_install': False,
    'license': "Other proprietary",
}
