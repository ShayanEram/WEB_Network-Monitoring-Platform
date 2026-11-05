# Network Monitoring Platform

A lightweight, real-time network monitoring platform featuring a high-performance C packet capture engine compiled via Zig, a Python Flask API backend with SQLite storage, and a minimalist light-mode frontend written in modular ES6 JavaScript.


## Tech Stack & Tooling Pipeline

* **Backend:** Python 3.13+, Flask, SQLite
* **Network Engine:** C language compiled via `zig cc` for cross-platform compatibility
* **Frontend:** Modular HTML5, CSS3, OOP ES6 JavaScript (Classes), Chart.js
* **Package Management:** `uv` (Fast Rust-based Python package manager)
* **Code Quality & Verification:**
  * **Python:** Ruff (Linter and Formatter)
  * **Web Stack:** ESLint v9+ & Prettier
  * **C Engine:** Clang-Format & Clang-Tidy

## First-Time Setup & Installation

### 1. Install Toolchain Dependencies

#### On Windows (PowerShell):
```powershell
# Install core package managers, runtimes, and compilers
winget install astral-sh.uv --silent --accept-source-agreements
winget install LLVM.LLVM --silent --accept-source-agreements
winget install zig.zig --silent --accept-source-agreements
winget install OpenJS.NodeJS.LTS --silent --accept-source-agreements

# Refresh environment PATH variables
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Allow execution of local scripts for workspace setup
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

#### On macOS:
```bash
brew install uv pre-commit llvm zig node
```

#### On Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3-pip pre-commit clang-format clang-tidy zig nodejs npm
pip install uv --break-system-packages
```

### 2. Initialize Workspace Dependencies

In the project root directory, run:
```bash
# 1. Create a virtual environment
uv venv

# 2. Synchronize Python dependencies
uv sync

# 3. Install JavaScript linting/formatting dependencies
npm install

# 4. Bind pre-commit hooks (using Python 3.13 environment isolation on Windows if needed)
uvx --python 3.13 pre-commit install
```

## Running the Application

To compile the C packet sniffer, initialize the database schema, start the daemon listener thread, and launch the Flask server, run:

```bash
uv run python app.py
```

Open your browser and navigate to: `http://127.0.0.1:5000`

## Development & Maintenance Commands

### Code Quality Verification

To run manual linting and formatting across the entire repository workspace:

```bash
uvx --python 3.13 pre-commit run --all-files
```

### Adding New Python Packages

To add new third-party dependencies with locked tracking:

```bash
uv add <package-name>
```

## Environment Cleanup / Teardown

If you need to reset the virtual environment, node modules, or local tool caches completely:

#### Reset Local Workspace Files:
```powershell
Remove-Item -Recurse -Force .venv, node_modules, package-lock.json
```

#### Full Toolchain Teardown (Windows PowerShell):
```powershell
winget uninstall astral-sh.uv --silent
winget uninstall LLVM.LLVM --silent
winget uninstall zig.zig --silent
winget uninstall OpenJS.NodeJS.LTS --silent

Remove-Item -Recurse -Force "$env:USERPROFILE\.uv" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\uv" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:USERPROFILE\.cache\pre-commit" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:APPDATA\npm-cache" -ErrorAction SilentlyContinue

Set-ExecutionPolicy Undefined -Scope CurrentUser -Force
```

## Continuous Integration

All branch commits and pull requests trigger automated GitHub Actions workflows (`.github/workflows/ci.yml`). The runner executes:
1. Python code formatting checks (Ruff)
2. ESLint & Prettier validations
3. Cross-platform C engine compilation tests via Zig

## Project Structure

```
WEB_Network-Monitoring-Platform/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .vscode/
│   └── settings.json
├── api/
│   └── routes.py
├── database/
│   ├── databaseHelper.py
│   └── schema.sql
├── models/
│   ├── alert.py
│   ├── device.py
│   └── traffic.py
├── network_engine/
│   ├── engine_runner.py
│   ├── packet_sniffer.c
│   └── packet_sniffer.h
├── static/
│   ├── css/
│   │   ├── about.css
│   │   ├── alerts.css
│   │   ├── base.css
│   │   ├── devices.css
│   │   ├── index.css
│   │   └── traffic.css
│   └── js/
│       ├── alerts.js
│       ├── devices.js
│       ├── index.js
│       └── traffic.js
├── templates/
│   ├── about.html
│   ├── alerts.html
│   ├── base.html
│   ├── devices.html
│   ├── index.html
│   └── traffic.html
├── .clang-format
├── eslint.config.js
├── .pre-commit-config.yaml
├── .prettierrc
├── app.py
├── config.py
├── package.json
├── pyproject.toml
└── uv.lock
```