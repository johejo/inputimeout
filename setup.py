from setuptools import setup, find_packages
try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

setup(
    name='inputimeout',
    version='0.1.1',
    author='Mitsuo Heijo',
    author_email='mitsuo_h@outlook.com',
    description='Standard input with timeout.',
    long_description=readme,
    packages=find_packages(),
    license='MIT',
    url='http://github.com/johejo/inputimeout',
    py_modules=['inputimeout'],
    keyword=['input', 'timeout'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
