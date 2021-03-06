#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = open('requirements.txt').readlines()

test_requirements = open('requirements-dev.txt').readlines()

setup(
    name='mailchute',
    version='0.1.0',
    description='A mailinator-like service providing disposable email address',
    long_description=readme + '\n\n' + history,
    author='Kevin J. Qiu',
    author_email='kevin@idempotent.ca',
    url='https://github.com/kevinjqiu/mailchute',
    packages=[
        'mailchute',
    ],
    package_dir={'mailchute':
                 'mailchute'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='mailchute',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'mailchute-smtpd=mailchute.smtpd.cli:main',
            'mailchute-api=mailchute.api.cli:main',
        ]
    },
)
