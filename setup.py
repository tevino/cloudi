from distutils.core import setup
import cloudi

setup(
    name='cloudi',
    version=cloudi.__version__,
    license=cloudi.__license__,
    author=cloudi.__author__,
    author_email=cloudi.__email__,
    packages=['cloudi', ],
    scripts=['scripts/d', ],
    url='https://github.com/tevino/cloudi',
    description='Convenient online EN<->ZH dictionary without other dependences for command line users.'
)
