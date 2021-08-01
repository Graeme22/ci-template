from setuptools import find_packages, setup

from src.utils import VERSION


f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='My Project',
    version=VERSION,
    description='A project that does things!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Graeme Holliday',
    author_email='graeme.holliday@pm.me',
    url='https://github.com/Graeme22/[repo-url]',
    license='MIT',
    install_requires=[
        # stuff!
    ],
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        app = src.app:main
    """,
)
