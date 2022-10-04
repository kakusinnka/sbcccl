import json

def log(severity, message):
    print(json.dumps(dict(severity=severity, message=message)))

log("DEFAULT", "DEFAULT message")
log("DEBUG", "DEBUG message")
log("INFO", "INFO message")
log("NOTICE", "NOTICE message")
log("WARNING", "WARNING message")
log("ERROR", "ERROR message")
log("CRITICAL", "CRITICAL message")
log("ALERT", "ALERT message")
log("EMERGENCY", "EMERGENCY message")