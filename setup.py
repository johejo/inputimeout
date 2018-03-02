from setuptools import setup, find_packages
import os
from codecs import open

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'inputimeout', '__version__.py'),
          'r', 'utf-8') as f:
    exec(f.read(), about)

tests_requirements = [
    'pytest-cov', 'pytest', 'flake8'
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=readme,
    packages=find_packages(),
    python_requires='>=3.4',
    license=about['__license__'],
    url=about['__url__'],
    py_modules=['inputimeout'],
    keyword=['input', 'timeout', 'stdin'],
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
    ],
    tests_requires=tests_requirements,
)
