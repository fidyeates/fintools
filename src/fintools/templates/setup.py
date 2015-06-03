from setuptools import setup, find_packages
setup(
    name="$NAME",
    version="0.1",
    packages=find_packages(),
    scripts=["bin/*"],

    install_requires=[],
    package_data={},

    # metadata for upload to PyPI
    author="",
    author_email="",
    description="",
    license="PSF",
    keywords="$NAME",
    url="",  # project home page, if any
)
