from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='dashmpeg',
    version='0.0.13',
    packages = find_packages(),
    author='Alisher M.',
    author_email='',
    description='Super simple wrapper around shaka-packager',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aliml92/dashmpeg',
    project_urls = {
        "Bug Tracker": "https://github.com/aliml92/dashmpeg/issues"
    },
    package_data={
      'dashmpeg': ['bin/*'],
    },
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    install_requires=[''],
)
