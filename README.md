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
winget install astral-sh.uv
winget install LLVM.LLVM
pip install pre-commit
```

2. Initialize Python Isolation Workspace

Run these commands in the root directory (Network-monitor/) to establish dependencies inside your locked workspace:
bash
#### Set up a pristine local virtual environment (.venv)
`uv venv`

#### Synchronize and install project requirements mapped in pyproject.toml
`uv sync`


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
