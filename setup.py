"""
Flask-JSONlocale
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-JSONLocale',
    version='1.1',
    url='http://example.com/flask-jsonlocale/',
    license='GNU',
    author='Martin Urbanec',
    author_email='martin@urbanec.cz',
    description='An extension for Flask allowing users to easily localize their Flask app',
    long_description=__doc__,
    py_modules=['flask_jsonlocale'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
	    'simplejson'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
