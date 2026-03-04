from setuptools import setup, find_packages

setup(
    name="greenhep", 
    version="0.1.0", 
    description="Sustainable Compression for High Energy Physics Workflows",
    author="Lyna",  
    url="https://github.com/Lynsoo/GreenHEP-Compression", 
    packages=find_packages(), 
    install_requires=[  
        "numpy==1.23.5",
        "pandas==1.5.3",
        "matplotlib==3.6.2",
        "zstandard==0.19.0",
        "uproot==4.2.3",
        "ROOT==6.26.06",  
    ],
    python_requires=">=3.8",  
    classifiers=[  
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True, 
)
