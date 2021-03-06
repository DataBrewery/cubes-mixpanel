from setuptools import setup, find_packages

requirements = ["pytz"]

setup(
    name = "cubes-mixpanel",
    version = '0.1',

    install_requires = requirements,

    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data = {
    },

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
    ],

    entry_points={
    },

    test_suite = "tests",

    # metadata for upload to PyPI
    author = "Stefan Urbanek",
    author_email = "stefan.urbanek@gmail.com",
    description = "Mixpanel Backend for Cubes Python OLAP",
    license = "MIT",
    keywords = "olap multidimensional data analysis",
    url = "http://cubes.databrewery.org"
)

