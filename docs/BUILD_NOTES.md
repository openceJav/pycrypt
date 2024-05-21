# Build Notes for Flask Project

**Pre-read**:
- [ ] [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
- [ ] [CONTRIBUTING.md](CONTRIBUTING.md)
- [ ] [README.md](README.md)
- [ ] [TODOs](TODOs.md)

This document serves as a guide for building the project. It will cover areas within the following domains:
- **Environment Setup**: Setting up the development environment from enabling tailwindCSS to running the flask application.
- **Project Structure**: Understanding the project structure and its components.
- **Commands Reference**: Collection of most used commands for the development of the flask application.

## Environment Setup

The environment is divided into two parts:
- **Frontend**: TailwindCSS ws/JavaScript
- **Backend**: Flask w/Python

The reason why I decided to go with tailwindCSS for the majority of the UI is due to its simplicity and ease-of-use when it comes to responsive and eye-catching designs. The backed is powered by Flask, with is considered as a micro framework for Python and is most definitely the easiest to get started with and setup. But there are some prerequisites that need to be installed before we can start the development.

There are 2 files that are important for setting up the initial environment: 
- `requirements.txt`: Contains all the dependencies used by python and for the backend.
- `package.json`: Contains all the dependencies used by tailwindCSS and for the frontend.

These are very important to install beforehand as they contain all the dependencies that are required for the project. Note that they will create their own seperate `/node_modules` and `./venv/` folders respectively.

## Project Structure

## Commands Reference