import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'wittypi'
AUTHOR = 'Olaf Wrieden'
AUTHOR_EMAIL = 'olaf@olafwrieden.com'
URL = 'https://github.com/olafwrieden/wittypi'

LICENSE = 'MIT'
DESCRIPTION = 'A Python wrapper library for the Witty Pi 3.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = []
SETUP_REQUIRES = ['pytest-runner']
TESTS_REQUIRE = ['pytest==4.4.1']

setup(
	name=PACKAGE_NAME,
	version=VERSION,
	description=DESCRIPTION,
	long_description=LONG_DESCRIPTION,
	long_description_content_type=LONG_DESC_TYPE,
	author=AUTHOR,
	license=LICENSE,
	author_email=AUTHOR_EMAIL,
	url=URL,
	install_requires=INSTALL_REQUIRES,
	packages=find_packages(include=['witty_pi']),
	setup_requires=SETUP_REQUIRES,
	tests_require=TESTS_REQUIRE
)