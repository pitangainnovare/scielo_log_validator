# SciELO Log Validator

The SciELO Log Validator project provides tools to validate log files for the SciELO platform. It supports Apache NCSA extended log format, BunnyCDN pipe-delimited format, IPv6 addresses, and IP list headers. It includes both command line and Python library usage options.

## Installation

To install the SciELO Log Validator, you can use `pip`:

```bash
pip install scielo-log-validator
```

Alternatively, you can clone the repository and install the dependencies manually:

```bash
git clone https://github.com/scieloorg/scielo_log_validator.git
cd scielo_log_validator
pip install -r requirements.txt
```

### Development setup

1. Clone the repository:
```bash
git clone https://github.com/scieloorg/scielo_log_validator.git
cd scielo_log_validator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in editable mode:
```bash
pip install -e .
```

5. Run tests:
```bash
python -m pytest
```

## Environment Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `DAYS_DELTA` | int | `30` | Maximum number of days between the file name date and the most probable content date for the log file to be considered valid. |
| `MIN_ACCEPTABLE_PERCENT_OF_REMOTE_IPS` | float | `3` | Minimum percentage of remote IPs required to consider the IP distribution valid. If the threshold is not met, the file is still accepted as long as remote IPs outnumber local IPs. |
| `MIN_NUMBER_OF_SAMPLE_LINES` | int | `1000` | Minimum number of lines in a file for the sample size to take effect. Files with fewer lines than this threshold are analyzed in full (sample size overridden to 1.0). |

## Usage

### Command line

```bash
log_validator [-h] -p PATH [-s SAMPLE_SIZE] [-b BUFFER_SIZE] [-d DAYS_DELTA]
              [--no_path_validation] [--no_content_validation]
```

| Argument | Default | Description |
|---|---|---|
| `-p`, `--path` | *(required)* | File or directory to validate. |
| `-s`, `--sample_size` | `0.1` | Fraction of lines to sample (0–1). |
| `-b`, `--buffer_size` | `2048` | Buffer size in bytes for MIME type detection. |
| `-d`, `--days_delta` | `5` | Days threshold for date consistency check. |
| `--no_path_validation` | — | Disable file-name validation. |
| `--no_content_validation` | — | Disable file-content validation. |

**Examples:**

```bash
# Validate a single file
log_validator -p /home/user/2022-03-01_scielo-br.log.gz

# Validate an entire directory
log_validator -p /home/user/
```

### Python library

```python
from scielo_log_validator import validator

# Validate a single file
result = validator.pipeline_validate(
    '/home/user/2022-03-01_scielo-br.log.gz',
    sample_size=0.25,
    apply_path_validation=True,
    apply_content_validation=True,
)

# Validate all files in a directory
import os
for root, _, files in os.walk('/home/user'):
    for file in files:
        file_path = os.path.join(root, file)
        result = validator.pipeline_validate(
            path=file_path,
            sample_size=0.1,
            apply_path_validation=True,
            apply_content_validation=True,
        )
```

### Result format

The output is a JSON object providing detailed validation information about the log file, including path details, content summary, and validation status:

```json
{
    "mode": {
        "path_validation": true,
        "content_validation": true
    },
    "path": {
        "date": "2022-03-01",
        "paperboy": false,
        "mimetype": "application/gzip",
        "extension": ".gz"
    },
    "content": {
        "summary": {
            "datetimes": {
                "(2022, 3, 1, 23)": 5,
                "(2022, 3, 2, 0)": 312,
                "(2022, 3, 2, 1)": 319
            },
            "invalid_lines": 0,
            "ips": {
                "local": 324,
                "remote": 10239,
                "unknown": 0
            },
            "total_lines": 10563
        }
    },
    "is_valid": {
        "ips": true,
        "dates": true,
        "all": true
    },
    "probably_date": "2022-03-02T00:00:00"
}
```

If the file cannot be read because it is corrupted, truncated, missing, or
inaccessible, `content` includes a structured error. A readable file that fails
the content rules does not include this error and is reported through
`is_valid` as usual.

```json
{
    "content": {
        "summary": {
            "total_lines": {
                "error": "File /logs/access.log.gz is corrupted"
            }
        },
        "error": {
            "code": "file_read_error",
            "kind": "corrupted",
            "message": "File /logs/access.log.gz is corrupted"
        }
    },
    "is_valid": {
        "ips": false,
        "dates": false,
        "all": false
    },
    "probably_date": {
        "error": "Date dictionary is empty"
    }
}
```

## Supported log formats

| Format | Description |
|---|---|
| NCSA Extended | Standard Apache combined log format with optional domain prefix and IP list fields. |
| BunnyCDN | Pipe-delimited format with Unix timestamps (7 or 10 digits), country codes, and request IDs. |
