# TestPlan_Generator

A Python tool to generate formatted test plans from YAML configuration files using Jinja2 templates and export as Word documents.

## Project Structure

- `configs/` - Contains YAML data and Jinja2 template files.
- `core/` - Core modules for loading YAML, rendering templates, and formatting DOCX.
- `gen_testplan.py` - Main script to generate test plans.
- `output/` - Folder where generated test plans are saved.

## Usage

1. Edit your YAML files in `configs/`.
2. Run `python gen_testplan.py` to generate the test plan DOCX.
3. Find the generated file in the `output/` folder.

## Requirements

- Python 3.x
- `pyyaml`
- `jinja2`
- `python-docx`

Install dependencies:

```bash
pip install pyyaml jinja2 python-docx

