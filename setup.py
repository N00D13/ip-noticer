from setuptools import setup

setup(name='ip-noticer',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/N00D13/ip-noticer',
      author='Alex Wellnitz',
      author_email='moin@wellnitz-alex.de',
      license='MIT',
      packages=['ipnoticer'],
      scripts=['bin/ip-noticer'],
      install_requires=[
          'twisted',
      ],
      zip_safe=False)