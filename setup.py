from setuptools import setup
import os

def open_file(fname):
   return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
   name="spicy_snake",            # name of your package
   version="0.0.1",
   description="a terminal-based snakegame",
   long_description=open_file("README.md"),  # only if you have a README.md
   author="Gülçin Vardar",
   author_email="gulcinv@gmail.com",
   packages=["spicy_snake"],      # same as name
   url="https://github.com/gulcinvardar/sriracha-snake",
   license="MIT",
   classifiers=[
      "Programming Language :: Python :: 3.9",
   ]
)