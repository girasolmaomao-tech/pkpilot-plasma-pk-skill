#!/usr/bin/env python3
import argparse
import os
import subprocess
from pathlib import Path


def resolve_binary(explicit_path: str = "") -> Path:
    candidates = [
        explicit_path,
        os.environ.get("PKPILOT_BIN", ""),
        str(Path.home() / ".local" / "bin" / "pkpilot"),
    ]
    for candidate in candidates:
        if candidate:
            path = Path(candidate).expanduser()
            if path.is_file() and os.access(path, os.X_OK):
                return path
    raise FileNotFoundError(
        "PKPilot runtime is not installed. Run scripts/install_pkpilot.sh after approving the download."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the local PKPilot Plasma PK binary.")
    parser.add_argument("--input", required=True, help="Path to a .xlsx or .csv input")
    parser.add_argument("--output", required=True, help="Output root directory")
    parser.add_argument("--binary", default="", help="Optional PKPilot binary path")
    parser.add_argument("--preview-only", action="store_true")
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    if not input_path.is_file():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if input_path.suffix.lower() not in {".xlsx", ".csv"}:
        raise ValueError("PKPilot accepts .xlsx or .csv; save legacy .xls files as .xlsx first.")

    output_path = Path(args.output).expanduser().resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    command = [
        str(resolve_binary(args.binary)),
        "--input",
        str(input_path),
        "--output",
        str(output_path),
    ]
    if args.preview_only:
        command.append("--preview-only")
    return subprocess.run(command, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
