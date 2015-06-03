from setuptools import setup, find_packages
setup(
    name="fintools",
    version="0.1",
    packages=find_packages(),
    scripts=["bin/start_project"],

    install_requires=[],
    package_data={},

    # metadata for upload to PyPI
    author="",
    author_email="",
    description="",
    license="PSF",
    keywords="fintools",
    url="",  # project home page, if any
)
