#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.md').read()

with open('requirements.txt') as reqs:
    requirements = reqs.read().split()

setup(
    name='py3wirecard',
    version='0.0.1',
    description='Wirecard API v2 Wrapper',
    author='Roberto Neves',
    author_email='robertonsilva@gmail.com',
    url='https://github.com/robertons/py3wirecard',
    packages=['py3wirecard'],
    package_dir={'py3wirecard': 'py3wirecard'},
    include_package_data=True,
    install_requires=requirements,
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Natural Language :: Portuguese (Brazilian)',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='wirecard, payment, payments, credit-card, boleto, moip'
)
