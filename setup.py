from setuptools import setup, find_packages
import os

version = '0.6.1'

setup(name='affinitic.caching',
      version=version,
      description="Caching function for affinitic projects",
      long_description=open("README.txt").read() + "\n" + open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=["Programming Language :: Python"],
      keywords='caching memcached',
      author='Jean-Francois Roche',
      author_email='jfroche@affinitic.be',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['affinitic'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(test=['zope.testing',
                                'zope.app.testing',
                                'sqlalchemy',
                                'zope.app.component']),
      install_requires=[
          'z3c.autoinclude',
          'setuptools',
          'grokcore.component',
          'zope.security',
          'zope.configuration',
          'zope.ramcache',
          'zope.event',
          'zope.component',
          'zope.app.cache',
          'plone.memoize',
          'lovely.memcached'])
