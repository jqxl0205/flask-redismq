"""
Flask-RedisMQ
-------------

Adds message queue using Redis support to your Flask application.

Links
`````

* `documentation <http://packages.python.org/Flask-RedisMQ>`_
* `development version
  <http://github.com/jqxl0205/flask-redismq/zipball/master#egg=Flask-RedisMQ-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-RedisMQ',
    version='0.1',
	url='http://github.com/jqxl0205/flask-redismq',
    license='BSD',
    author='He Weiwei',
    author_email='heww0205@gmail.com',
    description='Adds message queue using Redis support to your Flask application',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
		'hotqueue'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
