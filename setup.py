#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = []

tests_require = []

setup(
    name="scieloh5m5",
    version="1.9.6",
    description="Library to delivery H5 M5 Google Scholar metrics for the SciELO Journals",
    author="SciELO",
    author_email="scielo-dev@googlegroups.com",
    maintainer="SciELO Devs",
    maintainer_email="scielo-dev@googlegroups.com",
    url="http://github.com/scieloorg/scieloh5m5",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
    ],
    dependency_links=[],
    tests_require=tests_require,
    test_suite='tests',
    install_requires=install_requires
)
