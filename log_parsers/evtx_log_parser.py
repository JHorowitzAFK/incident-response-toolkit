
from Evtx.Evtx import Evtx

def parse_evtx_logs(file_path):
    with Evtx(file_path) as log:
        records = []
        for record in log.records():
            records.append(record.xml())
    return records
