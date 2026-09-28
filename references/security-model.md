# Distribution And Security Model

This public skill contains orchestration instructions, an installer, a standard-library wrapper, documentation, and a synthetic input template. It does not contain the PKPilot backend source or user study data.

The backend is distributed as an Apple Silicon Mach-O executable in GitHub Releases. The installer verifies a pinned SHA-256 checksum and the embedded ad-hoc code signature before installation. Analysis is local and the binary does not upload study data.

Compiled distribution prevents ordinary viewing of the original Python files, but no client-side binary can guarantee protection against expert reverse engineering. A hosted API would be required for stronger algorithm secrecy.

The current RC binary is ad-hoc signed, not Apple Developer ID signed or notarized. macOS may show a security warning. Do not bypass checksum or signature failures.
