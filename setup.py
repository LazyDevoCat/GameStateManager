import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GameStateMachine",
    version="0.0.1",
    author="Oleksii Bulba",
    author_email="oleksii.bulba@gmail.com",
    description="Game state machine - provides a game management based on a game state",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OleksiiBulba/GameStateManager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment"
    ],
    python_requires='>=3.8.2'
)
