'''
Build tools script
'''

from setuptools import setup, find_packages


setup(
    name="plant_scanner",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "package_name": ["assets/*"],
    },

    # Python Requires
    python_requires = ">=3.12",
    install_requires=[
        "pydantic==2.10.3",
        "pillow==11.0.0"
    ],

    classifiers=[
        "Development Status :: 4 - Beta",           # Status pengembangan
        "Intended Audience :: Developers",          # Audiens proyek
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",   # Lisensi
        "Programming Language :: Python",           # Bahasa pemrograman
        "Programming Language :: Python :: 3",      # Versi Python
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",       # Sistem operasi
        "Topic :: Scientific/Engineering :: Artificial Intelligence", 
        "Topic :: Software Development :: Libraries",
    ],
)
