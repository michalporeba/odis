from setuptools import find_packages, setup

def long_description():
    with open('README.md', 'r') as readme:
        return readme.read()

setup(
    name='django-kinder-settings',
    packages=find_packages(include=['django_kinder_settings']),
    version='0.1.8',
    author='Michal Poreba',
    license='MIT',
    description='A kinder sort of django settings',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/michalporeba/odis/packages/django-kinder-settings',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'Topic :: Software Development'
    ],
    install_requires=['django'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)