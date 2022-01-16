from setuptools import find_packages, setup

def long_description():
    with open('README.md', 'r') as readme:
        return readme.read()

setup(
    name='polymedia',
    packages=find_packages(include=['polymedia']),
    version='0.1.9',
    author='Michal Poreba',
    license='MIT',
    description='A polyglot hypermedia library for python ReSTful services',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/michalporeba/odis/packages/polymedia',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'Topic :: Software Development'
    ],
    install_requires=['requests', 'diogi', 'callouts', 'alps-py'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'responses'],
    test_suite='tests'
)