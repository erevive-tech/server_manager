from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in server_manager/__init__.py
from server_manager import __version__ as version

setup(
	name="server_manager",
	version=version,
	description="Server Manager System",
	author="RamjanAli Lal",
	author_email="ramjanali@erevivetechnologies.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
