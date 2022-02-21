import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup

pyspark = "^3.0.3"
chispa = "^0.8.3"
pytest = "^6.2.5"

INSTALL_REQUIRES = [
    "pyspark>=3.0.3",
    "chispa>=0.8.3",
    "pytest>=6.2.5",
    "pytest-spark>=0.6.0",    
    "pytest-cov>=2.12.1"        
]

setup(
    name="poetrydemo-pyspark",
    version="0.0.1",
    license="MIT",
    description="poetry-demo pyspark",
    long_description="",
    long_description_content_type="text/x-rst",
    author="Minyang Chen",
    author_email="mychen76@gmail.com",
    url="https://github.com/minyang-chen/poetry-demo/",
    packages=find_packages("src", exclude=("test*", "docs*")),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.5",
    keywords=" ".join(
        [
            "poetry",
            "pyspark",
            "tests"
        ]
    ),
    install_requires=INSTALL_REQUIRES,
    test_suite="tests"
)

s