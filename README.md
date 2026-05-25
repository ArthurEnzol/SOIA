# Soia

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Alpha-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey?style=for-the-badge)
![Shell](https://img.shields.io/badge/Shell-Bash%20%7C%20Zsh%20%7C%20Fish-success?style=for-the-badge)

### Intelligent Personal Assistant and Automation System

</div>

---

# Overview

**Soia** is a personal assistant built with Python focused on automation, workflow optimization, and developer productivity.

The project aims to provide a terminal-based assistant capable of organizing tasks, assisting with development workflows, and simplifying repetitive operations directly from the command line.

---

# Features

## Automation
Automate repetitive workflows and terminal tasks.

## Personal Assistance
Execute commands, organize information, and assist daily activities.

## Terminal Integration
Run the assistant globally through a simple shell command.

## Multi-Shell Support
Compatible with Bash, Zsh, and Fish shell environments.

---

# Technologies

## Backend
- Python

## Environment
- Virtual Environment (venv)

## Tools
- Git
- Shell Scripting

---

# Installation (Recommended)

The easiest way to install Soia is through the automatic installer.

---

## 1. Download the Installer

Using `curl`:

```bash
curl -O https://raw.githubusercontent.com/ArthurEnzol/Soia-Alpha/main/instalar-soia.sh
```

Or using `wget`:

```bash
wget https://raw.githubusercontent.com/ArthurEnzol/Soia-Alpha/main/instalar-soia.sh
```

---

## 2. Run the Installer

```bash
chmod +x instalar-soia.sh
./instalar-soia.sh
```

---

# What the Installer Does

The installer automatically:

- Creates the `~/SOIA` directory
- Clones the project repository
- Configures the `soia` command globally
- Detects Bash, Zsh, or Fish shell
- Prepares the virtual environment
- Leaves the system ready for use

---

# Usage

After installation, run Soia from any directory:

```bash
soia
```

---

## Run in Another Project Directory

```bash
soia /path/to/project
```

---

## Debug Mode

```bash
soia --modo debug
```

---

## Help Command

```bash
soia --ajuda
```

---

# Updating Soia

To update the project in the future, simply run the installer again:

```bash
./instalar-soia.sh
```

Or manually update the repository:

```bash
cd ~/SOIA/Soia-Alpha
git pull
```

---

# Requirements

- Python 3.10+
- Git
- Virtual Environment (`venv`)
- Linux-based environment
- Bash, Zsh, or Fish shell

---

# Project Structure

```bash
~/SOIA/
└── Soia-Alpha/
    ├── main.py
    ├── config.json
    ├── instalar-soia.sh
    ├── .venv/
    └── ...
```

---

# Concepts Practiced

- Python Automation
- Shell Scripting
- CLI Development
- Environment Configuration
- Linux Terminal Integration
- Virtual Environment Management

---

# Future Improvements

- AI-powered workflow assistance
- Plugin system
- Voice interaction support
- Cross-platform support
- Docker support
- GUI interface
- Cloud synchronization

---

# Support

If you encounter installation issues or bugs, feel free to open an Issue in the repository.

---

# Contributing

Contributions are welcome.

Feel free to fork the repository and submit improvements through pull requests.

---

# License

This project is licensed under the MIT License.

---

<div align="center">

Built with Python and terminal automation.

</div>
