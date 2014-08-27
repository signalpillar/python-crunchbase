from distutils.core import setup

long_description = open('README.md').read()

setup(name="python-crunchbase",
      version="2.0.1",
      py_modules=["crunchbase"],
      description="Libraries for interacting with the Crunchbase 2.0 API",
      author="Brian Anglin <brianranglin@gmail.com>",
      author_email="brianranglin@gmail.com",
      license="WTFPL",
      url="https://github.com/anglinb/python-crunchbase",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development" +
                   " :: Libraries :: Python Modules",
                   ],
      install_requires=["simplejson >= 1.8"]
      )
