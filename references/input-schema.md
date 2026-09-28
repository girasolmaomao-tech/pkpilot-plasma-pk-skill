# Input Schema

PKPilot accepts `.xlsx` templates and flat `.csv` files. Save legacy `.xls` files as `.xlsx` first.

Required fields are `study_name`, `sample_id`, `analyte`, `formulation`, `route`, `dose_mg_kg`, `animal_id`, `matrix_type`, `time_h`, `concentration`, and `concentration_unit`.

- Use one row per animal and time point.
- Set `matrix_type` to `plasma`.
- Use `PO`, `IV`, `SC`, or `IP` for route.
- Keep concentration units consistent within a study.
- Numeric concentrations and `BLQ`/`BLOQ` are accepted.
- Duplicate `animal_id + time_h + matrix_type` rows fail validation.
- Negative concentrations and blank required fields fail validation.

Use `assets/pk_input_template.xlsx` as the starting template.
