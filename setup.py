from setuptools import setup, find_packages
import glob

setup(
    name="fintools",
    version="0.1",
    package_dir={'': 'src'},
    packages=['fintools'],
    scripts=["bin/start_project"],
    data_files=[
        ("fintools/templates", [
            "src/fintools/templates/.gitignore",
            "src/fintools/templates/setup.py",
            "src/fintools/templates/README.md"]),
        ("fintools", ["src/fintools/project_layout.yaml"])
        ],
    install_requires=["virtualenv>=13.0.1", "virtualenvwrapper>=4.5.1", "PyYAML>=3.11"],
    package_data={
    },

    # metadata for upload to PyPI
    author="",
    author_email="",
    description="",
    license="PSF",
    keywords="fintools",
    url="",  # project home page, if any
)
