# Advanced Port Scanner + CVE Analyzer

## Overview
This tool is a lightweight network reconnaissance scanner built using Python standard libraries only.

It identifies open ports, maps them to known services, and correlates findings against a local CVE database to assess risk levels.

DISCLAIMER:
This is for educational, and authorized testing only; I bear no responsobility for legal issues or charges brought against you for using this tool, in any unethical or illegal way. 

Additionally, you may take this tool, and any of my projects, and use them and modify them as you wish, If you have suggesstions for my further cybersecurity portfolio or projects, you may contact me with your proposal, please allow me up to a week to respond, as I am a full time student, work full time, and run my own business. 

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
