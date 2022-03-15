from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = "owapi",
  version = "0.0.1",
  description = "An Overwatch API coded in Python. Returns json styled data.",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/kokonut27/owapi.py",
  author = "kokonut27",
  author_email = "beol0127@gmail.com",
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "MIT License",
  packages=['owapi'],
  project_urls={
    "Issues": "https://github.com/kokonut27/owapi.py/issues",
    "Pull Requests": "https://github.com/kokonut27/owapi.py/pulls"
    },
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)