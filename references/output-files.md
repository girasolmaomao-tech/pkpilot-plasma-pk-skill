# Output Files

Each run creates a study directory with `tables`, `figures`, `reports`, `ppt`, `logs`, and `_work` folders.

Core outputs:

- `plasma_pk_parameters.csv`: Mean-profile PK parameters.
- `plasma_pk_animal_parameters.csv`: Individual-animal PK parameters.
- `plasma_pk_parameter_summary.csv`: Animal-level mean and sample SD.
- `plasma_concentration_summary.csv`: Mean, SD, CV%, and n by time.
- `terminal_phase_audit.csv`: Candidate terminal fits for manual review.
- `plasma_pk_qc_flags.csv`: Sample and PK QC messages.
- `processed_report.xlsx`: Multi-sheet workbook.
- `report_pk_analysis.pptx`: Basic Plasma PK report.

Always review `auc_method_used`, `auc_extra_percent`, `lambda_z_points_used`, `lambda_z_r2`, `adjusted_R2`, `terminal_phase_start`, `terminal_phase_end`, and `pk_qc_flag`.
