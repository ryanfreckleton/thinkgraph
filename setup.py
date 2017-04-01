from distutils.core import setup

setup(
    name='thinkgraph',
    version='0.1.0',
    author='Ryan E. Freckleton',
    author_email='ryan.freckleton@gmail.com',
    packages=['thinkgraph'],
    scripts=['bin/thinkgraph.py'],
    url='http://pypi.python.org/pypi/thinkgraph/',
    license='LICENSE.txt',
    description='TBD',
    long_description=open('README.markdown').read(),
    install_requires=[
        "grako>=3.10.0",
        "graphviz>=0.6",
    ],
)
