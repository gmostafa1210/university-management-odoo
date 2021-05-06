{
    'name' : 'XYZ Uni (manifest,name)',
    'version' : '1.0',
    'summary': 'University Management',
    'sequence' : 5,
    'description' : 'XYZ Uni (manifest,description)',
    'depends' : ['base'],
    'data' : [
        'views/course_views.xml',
        'views/department_views.xml',
        'views/faculty_views.xml',
        'views/staff_views.xml',
        'views/student_views.xml',
        'views/university_views.xml'
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}