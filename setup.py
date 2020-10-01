import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))
    setup(
        name='spoken-english-to-written-english',
        packages=['spokenEng2WrittenEng'],
        version='0.1',
        license=open('LICENSE').read(),
        description='Convert Spoken English given as text to Written English ',
        author='Arpit Toshniwal',
        author_email='arpitbhl@gmail.com',
        url='https://github.com/arpitbhl/spoken-english-to-written-english',
        classifiers=[
            'Intended Audience :: Developers',
            'Programming Language :: Python'
        ]

    )
