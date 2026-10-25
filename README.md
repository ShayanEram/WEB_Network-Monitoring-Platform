# Network-monitor

```text
Network-monitor/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .vscode/
│   └── settings.json
├── api/
│   └── routes.py
├── database/
│   └── schema.sql
├── models/
│   ├── device.py
│   └── traffic.py
├── network_engine/
│   ├── Makefile
│   └── packet_sniffer.c
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── dashboard.js
├── templates/
│   ├── index.html
│   └── login.html
├── .clang-format
├── .eslint.config.js
├── .pre-commit-config.yaml
├── .prettierrc
├── app.py
├── config.py
├── pyproject.toml
└── uv.lock
```

## Environment Setup & Tooling Pipeline

This repository implements industry-standard automation tools for linting, formatting, environment isolation, and automated verification rules.
• Package Management: uv (Rust-based ultra-fast virtualenv manager)
• Python Stack: Ruff (Unified PEP 8 linter and formatter running at lightspeed)
• Web Stack: ESLint (Logic guardrails) + Prettier (Layout adjustments)
• C Core Engine: Clang-Tidy (Static bug analysis) + Clang-Format (Chromium code style layout)

## First-Time Installation

Follow these steps to establish your workspace dependencies and activate git hooks.

1. Install Global Core Binaries

Install the project manager (uv), the git hooks container (pre-commit), and the localized C toolchains on your platform:

On macOS (using Homebrew):
```bash
brew install uv pre-commit llvm
```

On Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3-pip pre-commit clang-format clang-tidy
pip install uv --break-system-packages
```

On Windows (using PowerShell / winget):
```powershell
# 1. Install all global package managers, engines, and toolchains silently
winget install astral-sh.uv --silent --accept-source-agreements
winget install LLVM.LLVM --silent --accept-source-agreements
winget install zig.zig --silent --accept-source-agreements
winget install OpenJS.NodeJS.LTS --silent --accept-source-agreements

# 2. Refresh the environment PATH immediately so your terminal sees the new tools
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# 3. Use 'uv' to cleanly isolate and install pre-commit globally
uv tool install pre-commit --python 3.13


```
---
# Installs package managers, C engines, and Node.js runtimes natively
winget install astral-sh.uv --silent --accept-source-agreements
winget install LLVM.LLVM --silent --accept-source-agreements
winget install zig.zig --silent --accept-source-agreements
winget install OpenJS.NodeJS.LTS --silent --accept-source-agreements

# Refreshes the terminal environment paths immediately
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# Creates a clean local isolated Python environment
uv venv

# Automatically handles, synchronizes, and locks your Python dependencies
uv sync

# Natively creates a perfectly encoded UTF-8 package.json to house web rules
node -e "fs.writeFileSync('package.json', JSON.stringify({ name: 'web-network-monitoring-platform', private: true, devDependencies: { eslint: '^9.0.0', prettier: '^3.0.0' } }, null, 2))"

# Downloads local ESLint and Prettier dependencies into node_modules/
npm install

# Bypasses Python 3.15 compilation locks to bind your automated Git hooks framework safely via Python 3.13
uvx --python 3.13 pre-commit install


---

2. Initialize Python Isolation Workspace

Run these commands in the root directory (Network-monitor/) to establish dependencies inside your locked workspace:
bash
#### Set up a pristine local virtual environment (.venv)
`uv venv`

#### Synchronize and install project requirements mapped in pyproject.toml
`uv sync`

# 1. Create a pristine local virtual environment (.venv)
uv venv

# 2. Synchronize and lock your Python ecosystem mapping
uv sync

# 3. Download local ESLint and Prettier modules for the Web stack
npm install

# 4. Bind the entire test & formatting ecosystem to your Git hooks
uv run pre-commit install

# 5. Run a complete system verification check across the directory
uv run pre-commit run --all-files



3. Connect Pre-Commit to Git Lifecycle

Link your formatting and linting pipelines to check code modifications before they register on your timeline:
bash
`pre-commit install`

Verification output: pre-commit installed at .git/hooks/pre-commit

## Usage Protocol

### Automatic Verification (On Local Commit)

Work normally with git commands. Rules run automatically to catch errors before code leaves your computer:
1. Stage changes: git add .
2. Attempt a save checkpoint: git commit -m "feat: analyze live icmp packets"
3. The automated test container runs tests sequentially.
	• If a structural rule fails, your file layout changes are modified automatically, and the commit pauses.
	• Simply check changes (git status), restage adjustments (git add .), and commit again.

### Manual Inspections (Entire Directory Execution)

If you want to clear styling inconsistencies across the full repository workspace tree at any point, run:
bash
`pre-commit run --all-files`


### Changing Third-Party Python Packs

Do not manually type dependencies into configuration tables. To add libraries securely with locked tracking metrics, use:
```bash
uv add name-of-package
```


## Integrated Editor Environment

Workspace variables are tracked in .vscode/settings.json. If you use Visual Studio Code, ensure you have the following marketplace extensions activated:
- Ruff (by Astral) — Real-time syntax errors and automated import organization.
- ESLint (by Microsoft) — Displays interface logical exceptions during script creation.
- Prettier (by Prettier) — Auto-formats layout patterns for web pages.
- C/C++ Extension Pack (by Microsoft) — Activates low-level evaluation tracking.

## Continuous Integration (CI Gate)

Every branch change pushed up to the cloud mirrors an ecosystem build inside GitHub Actions pipelines (.github/workflows/ci.yml). This build runner checks environment validation routines even if local hooks were skipped:
- Ensures code layout validation tests successfully clear formatting passes.
- Runs static analyzers to screen for security holes.
- Runs your localized compiler setup to ensure your engine compiles cleanly without breaks.
Now that the README matches your layout perfectly, would you like me to walk through how to build out your actual packet_sniffer.c file or connect it to your Python routes?

---
Remove-Item -Recurse -Force .venv, node_modules, package.json, package-lock.json
# Natively uninstall all globally added toolchains and managers
winget uninstall astral-sh.uv --silent
winget uninstall LLVM.LLVM --silent
winget uninstall zig.zig --silent
winget uninstall OpenJS.NodeJS.LTS --silent
# 1. Clear out all isolated uv tools and cached runtimes
Remove-Item -Recurse -Force "$env:USERPROFILE\.uv"
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\uv"

# 2. Clear out any cached pre-commit configuration blocks
Remove-Item -Recurse -Force "$env:USERPROFILE\.cache\pre-commit"

# 3. Clear npm cache records
Remove-Item -Recurse -Force "$env:APPDATA\npm-cache"

# 4. Revert script security back to the default safe Windows state (Undefined)
Set-ExecutionPolicy Undefined -Scope CurrentUser -Force

