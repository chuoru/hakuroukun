from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['traffic_cones_detection'],
    package_dir={'': ''},
)

setup(**setup_args)
