#from setuptools import find_packages
from setuptools import setup

setup(name='pre_commit_checks',
      entry_points = {
        'console_scripts': ['secrets_filecontent=secrets_filecontent:main', 'secrets_filename=secrets_filename:main'$
      }
      )

