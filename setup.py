#!/usr/bin/env python
# Python wrapper for the cbrf uuid library.
# Authors:
#    OkeyDJ (okeydj@gmail.com)

from setuptools import setup, find_packages, Extension
from setuptools.command.build_py import build_py as _build_py

class CustomInstallCommand(_build_py):
    def run(self):
        print("Compiling uuid_cbr library...")
        self.run_command("build_ext")
        return super().run()


setup(name='uuid_cbr',
      version='1.0.0',
      author='OkeyDJ <okeydj@gmail.com>',
      author_email='okeydj@gmail.com',
      description='Python wrapper for the cbrf uuid library.',
      long_description=open('README.rst').read(),
      cmdclass={'build_py': CustomInstallCommand},
      license='MIT',
      test_suite='tests',
      url='https://github.com/Okeydj/cbr-uuid-python',
      packages=["uuid_cbr"],
      ext_modules=[Extension('_uuid_cbr_c',
                             ['uuid_cbr/uuid_cbr.i', 'uuid_cbr/uid.c', 'uuid_cbr/uuid.c', 'uuid_cbr/uuid_cbr.c'],
                             include_dirs=["uuid_cbr"],
                             depends=['uuid_cbr/uuid_cbr.h'],
                             )])
