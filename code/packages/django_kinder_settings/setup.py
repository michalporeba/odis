from setuptools import find_packages, setup

setup(
    name='django_kinder_settings',
    packages=find_packages(include=['django_kinder_settings']),
    version='0.0.1',
    description='A kinder sort of django settings',
    author='Michal Poreba',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)