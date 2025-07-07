from setuptools import setup, find_packages

with open('requirements.txt') as f:
	requirements = f.read().strip().split('\n')

setup(
	name='frappe_mcp_app',
	version='0.0.1',
	description='Frappe MCP integration app for exposing Frappe tools to AI assistants',
	author='Chinmay Bhatk',
	author_email='your@email.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=requirements
)