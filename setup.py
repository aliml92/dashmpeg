import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mpegdashprep',
    version='0.0.1',
    author='Alisher M',
    author_email='alisherm@test.com',
    description='Super simple wrapper around shaka-packager',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aliml92/mpeg-dash-prep',
    project_urls = {
        "Bug Tracker": "https://github.com/aliml92/mpeg-dash-prep/issues"
    },
    license='MIT',
    packages=['mpegdashprep'],
    install_requires=['requests'],
)