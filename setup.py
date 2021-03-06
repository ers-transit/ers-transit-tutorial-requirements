"""
This setup.py file sets up our package to be installable on any computer,
so that folks can `import ers-transit-tutorial-requirements` from within any directory.

Thanks to this file, you can...

...tell python to look for code in the current directory (which you
can continue to edit), by typing *one* of the following commands:

`pip install -e .`
or
`python setup.py develop`

...move a copy of this code to your site-packages directory, where python will
be able to find it (but you won't be able to keep editing it), by typing *one*
of the following commands:

`pip install .`
or
`python setup.py install`

...upload the entire package to the Python Package Index, so that other folks
will be able to install your package via the simple `pip install exoplanet-chromatic`, by
running the following command:

`python setup.py release`

The template for this setup.py came was pieced together with help from
@christinahedges, @barentsen, @timothydmorton, and @dfm. Check them
out on github for more beautiful code!

[`python-packaging`](https://python-packaging.readthedocs.io/en/latest/index.html)
is a pretty useful resource too!
"""

# import our basic setup ingredients
from setuptools import setup, find_packages
import os, sys

# running `python setup.py release` from the command line will post to PyPI
if "release" in sys.argv[-1]:
    os.system("python setup.py sdist")
    # uncomment the next line to test out on test.pypi.com/project/tess-zap
    # os.system("twine upload --repository-url https://test.pypi.org/legacy/ dist/*")
    os.system("twine upload dist/*")
    os.system("rm -rf dist/ers-transit-tutorial-requirements*")
    sys.exit()

# a little kludge to get the version number from __version__
exec(open("erstransittutorialrequirements/version.py").read())

# run the setup function
setup(
    # the name folks can use to search for this with pip
    name="ers-transit-tutorial-requirements",
    # what version of the code is this?
    version=__version__,
    # what's a short description of the package?
    description="Installs the required packages for the ERS tutorials.",
    # what's a more detailed description?
    long_description="",
    # who's the main author?
    author="Zach Berta-Thompson",
    # what's the main author's email?
    author_email="zach.bertathompson@colorado.edu",
    # what's the URL for the repository?
    url="https://github.com/ers-transit/ers-transit-tutorial-requirements",
    # this figures out what subdirectories to include
    packages=find_packages(),
    # are there data that should be accessible when installed?
    include_package_data=True,
    # are there scripts to be copied into your $PATH?
    scripts=[],
    # some descriptions about this package (for searchability)
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    # what other packages are needed? (must be pip-installable)
    install_requires=[
        'jupyter',
        'matplotlib',
        'numpy',
        'scipy',
        'astropy',
        'bokeh',
        'h5py',
        'pandas',
        'pytest',
        'pyyaml',
        'requests',
        'nbsphinx',
        'tqdm',
        'lmfit',
        'batman-package',
        'dynesty',
        'emcee',
        'corner'],
    # what version of Python is required?
    python_requires=">=3.6",  # f-strings are introduced in 3.6!
    # requirements in `key` will install with `pip install exoplanet-chromatic[key]`
    extras_require={},
    # (I think just leave this set to False)
    zip_safe=False,
    # under what license is this code released?
    license="MIT",
)
