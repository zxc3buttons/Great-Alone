from setuptools import setup, find_packages

setup(
    name='mysite',
    version='1.0',
    author='Alex',
    author_email='sasha.saveylov@mail.ru',
    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py']
)
