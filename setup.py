from setuptools import setup, find_packages

setup(name="CENSUS-income",
      version="0.0.1",
      author="akash",
      author_email="tiwari1407akash@gmail.com",
      packages=find_packages(),
      install_requirements=["pandas","numpy","flask"]
      )