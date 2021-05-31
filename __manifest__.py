{
    'name' : 'XYZ University',
    'version' : '1.0',
    'summary': 'University Management',
    'sequence' : 5,
    'description' : 'XYZ University description.',
    'depends' : ['base','sale_management','stock','purchase'],
    'data' : [
        'security/university_security.xml',
        'security/ir.model.access.csv',

        'views/university_views.xml',
        'views/faculty_views.xml',
        'views/student_views.xml',
        'views/department_views.xml',
        'views/course_views.xml',
        'views/staff_views.xml',
        'views/inherit_staff_views.xml',
        'views/sale_inherit_views.xml',
        'views/sale_product_inherit_views.xml',
        'views/brand_dealer_views.xml',
        'views/purchase_extend_views.xml',

        'report/student_report.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}