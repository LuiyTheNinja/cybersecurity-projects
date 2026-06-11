# Advanced Port Scanner + CVE Analyzer

## Overview
This tool is a lightweight network reconnaissance scanner built using Python standard libraries only.

It identifies open ports, maps them to known services, and correlates findings against a local CVE database to assess risk levels.

## Features
- TCP port scanning
- Service identification
- CVE correlation (local database)
- Severity classification (Critical / High / Medium / Low)
- No external dependencies

## How It Works
1. Scans target ports using socket connections
2. Identifies common services based on port
3. Matches services against local CVE database
4. Outputs risk assessment

## Usage

```bash
python3 scanner.py
