
from log_parsers.text_log_parser import parse_text_logs
from log_parsers.evtx_log_parser import parse_evtx_logs
from detection.anomaly_detector import detect_anomalies
from detection.windows_event_detector import detect_event_ids
from utils.csv_exporter import export_to_csv
from utils.config_loader import load_config

def main():
    # Load configurations
    config = load_config("config.ini")

    # Parse text logs and detect anomalies
    text_log_data = parse_text_logs("sample_text_log.log")
    anomalies = detect_anomalies(text_log_data, config)

    # Parse .evtx files and detect event IDs
    evtx_log_data = parse_evtx_logs("sample_event_log.evtx")
    critical_events = detect_event_ids(evtx_log_data, config)

    # Export results to CSV
    export_to_csv(anomalies, critical_events, "detected_events.csv")

if __name__ == "__main__":
    main()
