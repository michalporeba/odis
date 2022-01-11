from setuptools import find_packages, setup

def long_description():
    with open('README.md', 'r') as readme:
        return readme.read()

setup(
    name='callouts',
    packages=find_packages(include=['callouts']),
    version='0.1.1',
    author='Michal Poreba',
    license='MIT',
    description='A simple, class based dispatcher',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/michalporeba/odis/packages/callouts',
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