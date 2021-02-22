#!/usr/bin/env python3

import psutil
import socket
import emails

sender = "automation@example.com"
recipient = "student-00-4dd743e70e3f@example.com"
body = "Please check your system and resolve the issue as soon as possible."

if psutil.cpu_percent(1) > 80:
    subject = "Error - CPU usage is over 80%"
    alert = emails.generate_alert(sender, recipient, subject, body)
    emails.send_email(alert)

if psutil.disk_usage('/')[3] > 80:
    subject = "Error - Available disk space is less than 20%"
    alert = emails.generate_alert(sender, recipient, subject, body)
    emails.send_email(alert)

if psutil.virtual_memory()[1] < (500 * (1024*1024)):
    subject = "Error - Available memory is less than 500MB"
    alert = emails.generate_alert(sender, recipient, subject, body)
    emails.send_email(alert)

if socket.getfqdn('127.0.0.1') != 'localhost':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    alert = emails.generate_alert(sender, recipient, subject, body)
    emails.send_email(alert)

