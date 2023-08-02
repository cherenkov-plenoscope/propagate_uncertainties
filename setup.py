import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="propagate_uncertainties_sebastian-achim-mueller",
    version="0.2.3",
    description="Propagate the uncertainty of multiple values",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/cherenkov-plenoscope/propagate_uncertainties",
    project_urls={
        "Bug Tracker": (
            "https://github.com/"
            "cherenkov-plenoscope/propagate_uncertainties/issues"
        ),
    },
    author="Sebastian Achim Mueller",
    author_email="sebastian-achim.mueller@mpi-hd.mpg.de",
    packages=["propagate_uncertainties",],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
    ],
)
