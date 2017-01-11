from setuptools import setup, find_packages

with open('README.md') as f:
  readme = f.read()

setup(
  name='ordergroove_scraper',
  version='0.1.0',
  description='OrderGroove Scraper excercise',
  long_description=readme,
  author='Matias Calcagno',
  author_email='mcalcagno@velocitypartners.net',
  url='https://github.com/kennethreitz/samplemod',
  packages=find_packages(exclude=('tests')),
  scripts=['bin/ordergroove-scraper']
)
