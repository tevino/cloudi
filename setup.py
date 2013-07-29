from distutils.core import setup

setup(
    name='cloudi',
    version='0.5.4',
    author='Tevin Zhang',
    author_email='mail2tevin@gmail.com',
    packages=['cloudi', ],
    scripts=['cloudi/d', ],
    url='https://github.com/tevino/cloudi',
    license='MIT',
    description='Convenient online En<->Zh dictionary for command line users.'
)
