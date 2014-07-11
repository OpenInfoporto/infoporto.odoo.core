# -*- coding: utf-8 -*-
"""
This module contains the tool of infoporto.odoo.core
"""
import os
from setuptools import setup, find_packages

version = '1.0'
setup(name='infoporto.odoo.core',
      version=version,
      description="Odoo core",
      long_description='',
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='Andrea Carmisciano',
      author_email='andrea.carmisciano@infoporto.it',
      url='http://www.infoporto.it',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['infoporto', 'infoporto.odoo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'setuptools',
            'plone.app.registry',
            'plone.app.dexterity [grok]',
                        ],
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
