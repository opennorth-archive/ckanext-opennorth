from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-opennorth',
    version=version,
    description="Mainly theming",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='St\xc3\xa9phane Guidoin',
    author_email='stephane@opennorth.ca',
    url='http://github.com/opennorth',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.opennorth'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        opennorth=ckanext.opennorth.plugin:OpennorthTemplatePlugin
        opennorthfacet=ckanext.opennorth.plugin:OpennorthFacetPlugin
        opennorthextrapages=ckanext.opennorth.plugin:OpennorthExtraPagesPlugin
    ''',
)
