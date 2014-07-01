from __future__ import print_function
from setuptools import setup
import io
import os

import passletters

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

setup(
    name='passletters',
    version=passletters.__version__,
    url='http://github.com/inversion/passletters',
    license='The MIT License',
    author='Andrew Moss',
    author_email='andrew@mossage.co.uk',
    description='Read password from stdin and echo it with letters enumerated. Clear terminal afterwards.',
    long_description=long_description,
    packages=['passletters'],
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        ],
    entry_points = {
        'console_scripts': [
            'passletters = passletters.passletters:main'
        ]
    }
)
