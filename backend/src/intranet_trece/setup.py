"""Installer for the intranet_trece package."""
from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="intranet_trece",
    version="1.0.0a1",
    description="Intranet TRE-CE configuration package.",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Marcos Viana",
    author_email="mviana75@gmail.com",
    url="https://github.com/mviana75/intranet-trece",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/intranet_trece",
        "Source": "https://github.com/mviana75/intranet-trece",
        "Tracker": "https://github.com/mviana75/intranet-trece/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "Plone",
        "prettyconf",
        "plone.api",
    ],
    extras_require={
        "test": [
            "pytest-plone>=0.2.0",
            "pytest-cov",
            "pytest",
            "gocept.pytestlayer",
            "zest.releaser[recommended]",
            "plone.app.testing[robot]>=7.0.0a3",
            "plone.restapi[test]",
            "collective.MockMailHost",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = intranet_trece.locales.update:update_locale
    """,
)
