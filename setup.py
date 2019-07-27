from setuptools import setup

setup(
    name='cifcheck',
    version='0.1',
    packages=['cifcheck'],
    url='',
    license='MIT',
    install_requires=[
        'jax', 'pymatgen', 'ase',  'scipy>=1.3.0rc1'
    ],
    extras_require={
        'testing': ['pytest', 'pytest-cov<2.6'],
        'docs': ['sphinx-rtd-theme', 'sphinxcontrib-bibtex'],
        'pre-commit': [
            'pre-commit==1.11.0', 'black', 'prospector==1.1.5',
            'pylint==1.9.3'
        ]
    },
    author='Kevin M. Jablonka',
    author_email='kevin.jablonka@epfl.ch',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 1 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    description=
    'small tool to check crystal structures')
