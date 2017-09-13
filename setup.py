#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 


import os
from setuptools import setup, find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

data_files = []
for dirpath, dirnames, filenames in os.walk('.'):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        continue
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])


setup ( name='django-banish-plus',
        version = "0.1",
        install_requires=['python-memcached',"celery"],
        description = "django-banish-plus is a django middleware to ban users, prevent too many concurrent connections and TOR ips request",
        long_description = long_description,
        author = "intelligenia S.L.",
        author_email = "josemiguel@intelligenia.com",
        url = "https://github.com/josemlp91/django-banish-plus",
        packages = find_packages('.'),
        license = 'Apache V2',
	data_files=data_files,
	keywords="tor banish security django",
        classifiers = [
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
	    'Development Status :: 5 - Production/Stable',
            'Framework :: Django',
        ],
     )
