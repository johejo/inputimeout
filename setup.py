from setuptools import setup, find_packages
from inputimeout import (
    __title__, __version__, __author__, __author_email__,
    __description__, __license__, __url__,
)

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''

setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description=readme,
    packages=find_packages(),
    license=__license__,
    url=__url__,
    py_modules=['inputimeout'],
    keyword=['input', 'timeout'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
    ]
)
