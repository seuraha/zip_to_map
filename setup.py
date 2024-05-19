from setuptools import setup, find_packages

setup(
    name="zip_to_map",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pgeocode>=0.5.0",
        "matplotlib>=3.6.2",
        "pandas>=2.1.2",
        "basemap>=1.4.1"
    ],
    entry_points={
        "console_scripts": [
            "zipcode_to_map=zip_to_map.zip_to_map:zipcode_to_map"
        ]
    },
    author="Seura Ha",
    author_email="seura@umich.edu",
    description="A library to plot zipcodes on a map. Currently support only US zipcodes.",
    url="https://github.com/seuraha/zip_to_map",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
