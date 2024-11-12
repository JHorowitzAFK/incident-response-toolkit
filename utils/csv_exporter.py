
import csv

def export_to_csv(anomalies, critical_events, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Details'])
        for anomaly in anomalies:
            writer.writerow(['Anomaly', anomaly])
        for event in critical_events:
            writer.writerow(['Critical Event', event])
