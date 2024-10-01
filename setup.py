from setuptools import setup, find_packages

# Read requirements from files
def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

requirements = parse_requirements('requirements.txt')
dev_requirements = parse_requirements('requirements_dev.txt')

setup(
    name="xray-lungs-prediction",
    version="0.1.0",
    author="Mohammad Shuaib",
    author_email="mohammadshuaib3455@gmail.com",
    description="A package for predicting lung conditions from X-ray images using deep learning",
    url="https://github.com/MohammadShuaib00/xrayLungsPrediction.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,  # Make sure this is a list of strings
    },
)
