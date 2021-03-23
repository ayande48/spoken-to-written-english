import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(name = 'SpokenToWritten',
      packages = ['SpokenToWritten'],
      version = '0.1',
      description = 'Convert a paragraph of Spoken English to Written English',
      author = 'Ayan De',
      author_email = 'ayande48@gmail.com',
      url = 'https://github.com/ayande48/Spoken-To-Written-English',
      classifiers = ['Intended Audience :: Developers', 'Programming Language :: Python'])