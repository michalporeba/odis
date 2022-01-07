from setuptools import find_packages, setup

def long_description():
    with open('README.md', 'r') as readme:
        return readme.read()

setup(
    name='wstl',
    packages=find_packages(include=['wstl']),
    version='0.0.1',
    author='Michal Poreba',
    license='MIT',
    description='A WSTL library for python ReSTful services',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/michalporeba/toposearch/packages/wstl',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'Topic :: Software Development'
    ],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)