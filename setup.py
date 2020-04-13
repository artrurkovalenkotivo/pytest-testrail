from setuptools import setup


def read_file(fname):
    with open(fname) as f:
        return f.read()


setup(
    name='pytes-_testrail',
    description='pytest plugin for creating TestRail runs and adding results',
    long_description=read_file('README.rst'),
    version='2.8.4',
    author='UTAF',
    author_email='UTAF',
    url='http://github.com/allankp/pytest-testrail/',
    packages=[
        'pytest_testrail',
    ],
    package_dir={'pytest_testrail': 'pytest_testrail'},
    install_requires=[
        'pytest>=3.6',
        'requests>=2.20.0',
    ],
    include_package_data=True,
    entry_points={'pytest11': ['pytes-testrail = pytest_testrail.conftest']},
)
