# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.4] - 2022-06-07
### Changed
- Marked all "abstract" methods with "@abstractmethod" from ABC package, removed raising an exception;
- Removed any transition data inside game states and moved it to return values of the method "end" and argument of the method "start";
- Added method descriptions;
- Removed Clock class, removed any clock logic from GameStateEngine, now every game state class can define own logic how often the game loop should go;
- Added more abstract methods to BaseGameState class;

## [0.0.3] - 2022-06-04
### Changed
- Project refresh;
- Added Makefile with commands for package building;
- Added MANIFEST.in file for including files into distributed package;
- Added requirements.txt file (no requirements so far, the package does not depend on pygame);
- Added version.txt file;
- Added method before_quit to state, this method is run for all states before app is closed;
- Added type float to time_delta argument in state run method;
- Dumped minimum python requirements to 3.8.10 (was 3.8.2);

## [0.0.2] - 2022-02-12
### Changed
- If initial_state_name is empty do not set it;

### Fixed
- Fixed a bug when initial state was started two times;

## [0.0.1] - 2020-11-02
Project created
### Added
- Created game state engine and base state classes;
- Added GNU General Public License v3.0;
- Created CHANGE.md and README.md files;