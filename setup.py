import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
requires = open(os.path.join(here, 'requirements.txt')).read().split('\n')

setup(name='tilegeoformats',
      version='0.0',
      description='tilegeoformats',
      classifiers=[],
      author='',
      author_email='',
      url='',
      keywords='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="testgeoformats",
      entry_points="""\
      [paste.app_factory]
      main = tilegeoformats:main
      """,
      )
