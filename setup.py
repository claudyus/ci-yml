"""
Installer for ci-yml
"""
import subprocess

try:
        from setuptools import setup, find_packages
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages

def git_version():
    try:
        return subprocess.check_output('git describe --always --tags', shell=True).strip()
    except:
        return "0.2"

setup(
    name='ci-yml',
    description='A .ci.yml parser for Gitlab-CI',
    long_description=open('README.rst').read(),
    version=git_version(),
    author='Claudio Mignanti',
    author_email='c.mignanti[at]gmail[dot]com',
    url='http://github.com/claudyus/ci-yml',
    packages=find_packages(exclude=['ez_setup']),
    scripts=['bin/ci-yml'],
    install_requires=open('requirements.txt').readlines(),
    include_package_data=True,
    download_url='https://github.com/claudyus/ci-yml/tarball/{}'.format(git_version()),
#   extras_require={
#       'plugins': open('extras_requirements.txt').readlines(),
#   },
    license='MIT'
)