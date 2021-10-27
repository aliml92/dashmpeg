import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mpegdash',
    version='0.0.8',
    author='Alisher M',
    author_email='alisherm@test.com',
    description='Super simple wrapper around shaka-packager',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aliml92/mpegdash',
    project_urls = {
        "Bug Tracker": "https://github.com/aliml92/mpegdash/issues"
    },
    license='MIT',
    packages=['mpegdash'],
    install_requires=['requests'],
)
