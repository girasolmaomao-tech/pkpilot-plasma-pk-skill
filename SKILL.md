---
name: pkpilot-plasma-pk
description: "Install and run PKPilot's local binary for auditable noncompartmental plasma pharmacokinetic analysis from Excel or CSV. Use for mean and animal-level Cmax, Tmax, AUC0-last, AUC0-inf, lambda-z, t1/2, QC flags, terminal-phase audit, plots, Excel, and PowerPoint outputs."
---

# PKPilot Plasma PK

Use the signed/checksummed PKPilot CLI binary. The backend source is not part of this skill.

## Supported Platform

- macOS on Apple Silicon (`arm64`)
- Local analysis only; no study data is uploaded by PKPilot
- `.xlsx` and `.csv` inputs

## Install The Runtime

1. Resolve the skill directory containing this file.
2. Check for the runtime:

   ```bash
   ${PKPILOT_BIN:-$HOME/.local/bin/pkpilot} --version
   ```

3. If missing, explain that installation downloads and executes a precompiled GitHub Release binary. Obtain the user's permission before running:

   ```bash
   bash <skill-dir>/scripts/install_pkpilot.sh
   ```

4. The installer must verify the SHA-256 checksum and ad-hoc code signature. Stop if either check fails.

## Analyze Data

1. Read [references/input-schema.md](references/input-schema.md).
2. Use a new output directory; never overwrite source data.
3. Run:

   ```bash
   python3 <skill-dir>/scripts/run_pk_analysis.py \
     --input <input.xlsx-or-csv> \
     --output <output-directory>
   ```

4. Inspect the generated CSVs. Report the result directory, Cmax, Tmax, AUC0-last, AUC0-inf, lambda-z, t1/2, QC flags, selected terminal points, and PPT status.
5. Treat `terminal_phase_audit.csv` as diagnostic evidence. Do not silently force terminal points to match reference software.

## Scientific Guardrails

- The validated default AUC method is linear trapezoidal.
- Lambda-z requires at least three post-Cmax positive points and uses adjusted-R2 selection with terminal rebound exclusion.
- Missing lambda-z/t1/2 must not invalidate Cmax, Tmax, or AUC.
- Surface `pk_qc_flag`, `auc_extra_percent`, `lambda_z_points_used`, R2, and adjusted R2.
- Do not present the output as regulator-validated or use it for clinical dosing decisions.

## Input Template

Use `assets/pk_input_template.xlsx` only as a field and workbook-layout reference. Its example rows are synthetic and should be replaced with the user's study data before analysis.

Read [references/output-files.md](references/output-files.md) for the artifact contract and [references/security-model.md](references/security-model.md) for the binary distribution model.
