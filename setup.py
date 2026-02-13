from setuptools import setup, find_packages

setup(
    name="fasta-basic-stats",
    version="0.1.0",
    description="Command-line tool to analyze FASTA files and generate comprehensive reports",
    author="Musi Anoh Didier Mandi",
    author_email="didiermusi09@gmail.com",
    url="https://github.com/didieranoh/fasta_basic_stats",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "fasta-basic-stats=fasta_tool.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
)
