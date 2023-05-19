from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()


setup(
    name = 'reefsafesunscreen',
    version = '0.0.1',
    author = 'Maci Schaub',
    author_email = 'macischaub@gmail.com',
    license = 'MIT',
    description = 'Programs to scrape, clean, and load data for'
                  ' Tableau dashboard to investigate sunscreens sold in Hawaii',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/margaretschaub/Sunscreen',
    py_modules = ['cleaning', 'scrapers', 'sql_files'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],

)