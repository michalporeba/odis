from setuptools import find_packages, setup


def long_description():
    with open("README.md", "r") as readme:
        return readme.read()


setup(
    name="alps-py",
    packages=find_packages(include=["alps"]),
    version="0.1.4",
    author="Michal Poreba",
    license="MIT",
    description="An ALPS library for python",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/michalporeba/odis/packages/alps/",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    install_requires=["diogi"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
