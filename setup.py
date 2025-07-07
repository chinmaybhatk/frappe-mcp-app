from setuptools import setup, find_packages

setup(
    name='frappe_mcp_app',
    version='0.0.1',
    description='MCP integration for Frappe',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "frappe-mcp"
    ],
)
