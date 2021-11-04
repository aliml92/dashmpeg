import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dashmpeg',
    version='0.0.6',
    author='Alisher M.',
    author_email='',
    description='Super simple wrapper around shaka-packager',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aliml92/dashmpeg',
    project_urls = {
        "Bug Tracker": "https://github.com/aliml92/dashmpeg/issues"
    },
    license='MIT',
    include_package_data=True,
    packages=['dashmpeg'],
    install_requires=[''],
)
