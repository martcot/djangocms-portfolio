import os
from setuptools import setup, find_packages


def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangocms-portfolio',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GNU General Public License',
    description='Widget Reservit for DjangoCMS',
    long_description=read('README.md'),
    url='https://github.com/Pyc0kw4k/djangocms-portfolio',
    author='Lozano Joaquim',
    #install_requires=["django-cors-headers==2.1.0"],
    author_email='joaquimlozano@gmail.com',
)