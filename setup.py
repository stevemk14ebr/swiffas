from setuptools import setup

setup(name='swiffas3',
      version='0.2',
      description='SWF parser and AVM2 (Actionscript 3) bytecode parser',
      url='https://github.com/stevemk14ebr/swiffas',
      author='Alex Hixon',
      author_email='alex@alexhixon.com',
      license='MIT',
      packages=['swiffas3'],
      install_requires=[
      	'bitstring'
      ],
      zip_safe=False)
