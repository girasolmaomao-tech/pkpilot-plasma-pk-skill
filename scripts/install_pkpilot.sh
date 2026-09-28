#!/usr/bin/env bash
set -euo pipefail

VERSION="v1.0.0-rc1-binary"
ASSET="pkpilot-cli-macos-arm64"
SHA256="03d4c3c70984bdd11b8c5d154a9824889592942cc0499aca6b15b8a2b5357049"
URL="https://github.com/girasolmaomao-tech/pkpilot-plasma-pk-skill/releases/download/${VERSION}/${ASSET}"
INSTALL_ROOT="${PKPILOT_INSTALL_DIR:-$HOME/.local/share/pkpilot}"
BIN_DIR="${PKPILOT_BIN_DIR:-$HOME/.local/bin}"
TARGET="$INSTALL_ROOT/$VERSION/$ASSET"
LINK="$BIN_DIR/pkpilot"

if [[ "$(uname -s)" != "Darwin" || "$(uname -m)" != "arm64" ]]; then
  echo "PKPilot $VERSION currently supports Apple Silicon macOS only." >&2
  exit 2
fi

tmp_file="$(mktemp -t pkpilot-cli.XXXXXX)"
trap 'rm -f "$tmp_file"' EXIT

echo "Downloading $URL"
curl --fail --location --proto '=https' --tlsv1.2 "$URL" --output "$tmp_file"
echo "$SHA256  $tmp_file" | shasum -a 256 --check
chmod 755 "$tmp_file"
codesign --verify --verbose=2 "$tmp_file"

mkdir -p "$(dirname "$TARGET")" "$BIN_DIR"
mv "$tmp_file" "$TARGET"
ln -sfn "$TARGET" "$LINK"
trap - EXIT

echo "Installed PKPilot: $LINK"
"$LINK" --version
