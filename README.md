# PKPilot Plasma PK Skill

PKPilot is an installable Codex skill for local, auditable noncompartmental Plasma PK analysis. The public repository contains only the skill wrapper and documentation; the PK/NCA backend is distributed as a compiled GitHub Release binary.

## Platform

- macOS Apple Silicon (`arm64`)
- `.xlsx` and `.csv` inputs
- Local processing with no study-data upload

## Install The Skill

```bash
git clone https://github.com/girasolmaomao-tech/pkpilot-plasma-pk-skill.git \
  ~/.codex/skills/pkpilot-plasma-pk
```

Restart Codex, invoke `$pkpilot-plasma-pk`, and approve the binary download when prompted. For manual runtime installation:

```bash
bash ~/.codex/skills/pkpilot-plasma-pk/scripts/install_pkpilot.sh
```

## Run

```bash
python3 scripts/run_pk_analysis.py \
  --input /path/to/input.xlsx \
  --output /path/to/output
```

Use `assets/pk_input_template.xlsx` as a field and workbook-layout reference. Replace its synthetic example rows with your own study data before analysis.

## Outputs

PKPilot generates mean and animal-level PK CSVs, terminal-phase audit data, QC flags, concentration-time plots, `processed_report.xlsx`, and `report_pk_analysis.pptx`.

## Source And Licensing

- Skill wrapper and documentation: MIT License.
- PKPilot compiled backend: [Binary Evaluation License](BINARY_LICENSE.md).
- The backend source is not included in this repository.

The binary is intended for research and evaluation, not regulated submission, clinical dosing, or medical decisions. Automatic terminal-phase selection requires qualified review.
