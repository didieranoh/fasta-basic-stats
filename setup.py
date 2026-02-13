from setuptools import setup, find_packages

setup(
    name="fasta-tool",                # The package name
    version="0.1.0",                  # Version
    description="CLI tool to analyze FASTA files and generate full reports",
    author="Your Name",
    author_email="you@example.com",
    url="https://github.com/yourusername/fasta_basic_stats",  # GitHub repo URL
    packages=find_packages(),         # Automatically finds fasta_tool package
    python_requires=">=3.8",          # Minimum Python version
    entry_points={
        "console_scripts": [
            "fasta-tool=fasta_tool.cli:main",  # Creates 'fasta-tool' command
        ],
    },
    install_requires=[],              # No extra dependencies for now
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
