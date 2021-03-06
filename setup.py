from setuptools import find_packages, setup

version='0.3'

try:
    long_description = open("README.txt").read()
except:
    long_description = ''

setup(name='trac-WorkflowActionButtons',
      version=version,
      description="Adds one-click buttons to Trac tickets for workflow operations (closing, reassigning, commenting)",
      long_description=long_description,
      author='Ethan Jucovy',
      author_email='ejucovy@gmail.com',
      url='http://trac-hacks.org/wiki/WorkflowActionButtonsPlugin',
      keywords='trac plugin',
      license="BSD",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests*']),
      package_data={
          'workflow_actionbuttons': [
              'htdocs/fontawesome/css/*.css',
              'htdocs/fontawesome/fonts/*.*',
              'htdocs/main/*.css',
              'htdocs/main/*.js',
              'htdocs/jquery.modal/*.css',
              'htdocs/jquery.modal/*.js',
              'htdocs/jquery.modal/*.png',
          ],
      },
      zip_safe=False,
      entry_points = """
      [trac.plugins]
      workflow_actionbuttons = workflow_actionbuttons
      """,
      )
