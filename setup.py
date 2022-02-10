from setuptools import setup

setup(name='molconfviewer', 
      version='0.0.2',
      author='Benoit Baillif',
      author_email='benoit.baillif@gmail.com',
      packages=['molconfviewer'],
      scripts=[],
      url='http://pypi.python.org/pypi/molconfviewer/',
      license='LICENSE.txt',
      description='Package to visualize molcules and their conformations in Jupyter',
      long_description=open('README.md').read(),
      install_requires=["py3dmol"]) # and rdkit, but install is with conda