from setuptools import setup, find_packages
setup(
    name='mypackage',
    version= '',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=['numpy']
)