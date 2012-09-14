from distutils.core import setup

setup(
    name='cloudi',
    version='0.4.2',
    author='Tevin Zhang',
    author_email='mail2tevin@gmail.com',
    packages=['cloudi', ],
    scripts=['cloudi/d', ],
    url='https://github.com/Tevino/cloudi',
    license='MIT',
    description='Convenient online En<->Zh dictionary for command line users.',
    long_description=open('README').read(),
)
