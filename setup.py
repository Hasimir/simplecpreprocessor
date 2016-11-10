from __future__ import absolute_import
from setuptools import setup
import json
import version_handling

version = "%s.%s.%s" % version_handling.get_version()

long_description="""TravisCI results                                        
    .. image:: https://travis-ci.org/nanonyme/simplecpreprocessor.svg?tag=v%s
""" % version


setup(
    name = "simplecpreprocessor",
    version = version,
    author = "Seppo Yli-Olli",
    author_email = "seppo.yli-olli@iki.fi",
    description = "Simple C preprocessor for usage eg before CFFI",
    keywords = "python c preprocessor",
    license = "BSD",
    url = "https://github.com/nanonyme/simplecpreprocessor",
    py_modules=["simplecpreprocessor"],
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        ],
    )
