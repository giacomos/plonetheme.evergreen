from setuptools import setup, find_packages
import os

setup(
        name='plonetheme.evergreen',
        description='An installable Diazo theme for Plone 4.1',
        long_description=open('README.rst', 'rb').read(),
        version='1.0',
        author='Giacomo Spettoli',
        author_email='giacomo.spettoli@gmail.com',
        url='http://svn.plone.org/svn/collective/plonetheme.evergreen',
        packages=find_packages(),
        include_package_data=True,
        namespace_packages=[
            'plonetheme'
            ],
        install_requires=[
            'setuptools',
            'plone.app.theming',
            ],
        classifiers=[
            "Framework :: Plone",
            "Programming Language :: Python",
            ],
        entry_points={
            'z3c.autoinclude.plugin': 'target = plone',
            }
        )


