
# Incident Response Toolkit

This Python-based toolkit was developed to assist incident responders in analyzing log files and detecting suspicious activities. 
Originally conceived during my time in law enforcement, this project has since been adapted for use in corporate investigations 
in the private sector, drawing on both public sector and private sector experience to detect threats efficiently.

## Features

- **Log Parsing**: Ingests both text log files (e.g., SSH logs, web server logs) and Windows Event Log (.evtx) files.
- **Anomalous Activity Detection in Text Logs**: Detects failed login attempts, suspicious IP addresses, privilege escalation, 
  unusual command executions, and access to sensitive directories.
- **Key Event Detection in Windows Logs**: Monitors important Event IDs (e.g., 4624, 4625) with customizable configurations.
- **Customizable Patterns**: Allows users to define additional patterns or Event IDs for both text and .evtx files.
- **CSV Export**: Exports detected events to a CSV file for further analysis.

## Getting Started

1. Clone the repository.
2. Configure `config.ini` to set up patterns and Event IDs.
3. Run `main.py` to begin log parsing and anomaly detection.
4. Check the generated CSV for a summary of detected events.

