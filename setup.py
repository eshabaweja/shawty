from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="shawty",
    version="0.0.1",
    description="shawty is a URL shortener.",
    author="eshabaweja",
    url="https://github.com/eshabaweja/shawty",
    license="Apache 2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
)