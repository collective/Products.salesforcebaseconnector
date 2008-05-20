from setuptools import setup, find_packages
import os

version = open(os.path.join("Products", "salesforcebaseconnector", "version.txt")).read().strip()

setup(name='Products.salesforcebaseconnector',
      version=version,
      description="",
      long_description=open(os.path.join("Products", "salesforcebaseconnector", "README.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Zope2",
        "Framework :: Plone",
        ],
      keywords='Zope CMF Plone Salesforce.com CRM integration',
      author='Plone/Salesforce Integration Group',
      author_email='plonesf@googlegroups.com',
      url='http://groups.google.com/group/plonesf',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'beatbox>=0.9,<=1.0dev',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )