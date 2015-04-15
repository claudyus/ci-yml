"""
Installer for ci-yml
"""

import shutils

try:
        from setuptools import setup, find_packages
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
setup(
    name='ci-yml',
    description='A .ci.yml parser for Gitlab-CI',
    long_description=open('README.rst').read(),
    version='unreleased', #FIXME
    author='Claudio Mignanti',
    author_email='c.mignanti[at]gmail[dot]com',
    url='http://github.com/claudyus/ci-yml',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=open('requirements.txt').readlines(),
    include_package_data=True,
    extras_require={
        'plugins': open('extras_requirements.txt').readlines(),
    },
    entry_points={
        'console_scripts': ['ci-yml = ci-yml:main',],
    },
    license='MIT'
)