# Technical Due Diligence Playbook

This repository provides a structured playbook for conducting
technical due diligence on potential vendors, acquisitions, or
partners.  It includes a checklist of areas to assess, guidance on
interview questions, and report templates.  The goal is to surface
risks, evaluate architectural soundness, and inform business
decisions.

## Components

- **Checklist**: A Markdown file (`checklist.md`) listing topics to
  cover such as architecture, security, scalability, code quality,
  documentation, and team practices.
- **Questions**: Suggested questions to ask during interviews or
  document reviews.
- **Report template**: A skeleton (`report_template.md`) to capture
  findings and recommendations.
- **CLI**: A small script (`playbook.py`) that can generate a new
  report file populated with the target, author, and date. Use the checklist
  alongside the generated report.

## Using the Playbook

Read through `checklist.md` and tailor it to the specific
engagement.  Use `playbook.py` to start a new report:

```bash
python -m pip install -r requirements.txt
python playbook.py --target "Vendor X" --output reports/vendor_x.md
```

Fill out the report with notes, risks, and recommendations as you
proceed through the due diligence. Use a new output path for each report.
The CLI preserves existing reports when a path is reused.