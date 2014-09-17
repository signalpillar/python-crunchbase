from distutils.core import setup

long_description = open('README.md').read()

setup(name="python-crunchbase",
      version="1.0.1",
      packages=["crunchbase"],
      description="Libraries for interacting with the Crunchbase 2.0 API",
      author="Brian Anglin <brianranglin@gmail.com>",
      author_email="brianranglin@gmail.com",
      license="WTFPL",
      url="https://github.com/anglinb/python-crunchbase",
      long_description=long_description,
      download_url = 'https://github.com/anglinb/python-crunchbase/tarball/1.0.1',
      platforms=["any"],
      classifiers=["Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development" +
                   " :: Libraries :: Python Modules",
                   ],
      keywords = ['crunchbase','2.0','api']
      )
