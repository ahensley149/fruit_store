#!/usr/bin/env python3

import os
from datetime import datetime
import reports
import emails

def get_fruit_data(directory):
    fruit_data = []
    for files in os.listdir(directory):
        with open(directory+files) as file:
            data = file.read().split('\n')
            fruit_data.append({'name': data[0], 'weight': data[1]})
    return fruit_data

def pdf_fruit_data(fruit_data):
    pdf_fruit = ''
    for fruit in fruit_data:
        if pdf_fruit == '':
            pdf_fruit = 'name: {}<br />weight: {}'.format(fruit['name'], fruit['weight'])
        else:
            pdf_fruit = pdf_fruit + '<br /><br />name: {}<br />weight: {}'.format(fruit['name'], fruit['weight'])
    return pdf_fruit

def email_fruit_data(fruit_data):
    email_fruit = ''
    for fruit in fruit_data:
        if email_fruit == '':
            email_fruit = 'name: {}\nweight: {}'.format(fruit['name'], fruit['weight'])
        else:
            email_fruit = email_fruit + '\n\nname: {}\nweight: {}'.format(fruit['name'], fruit['weight'])
    return email_fruit

if __name__ == "__main__":
    fruit_data = get_fruit_data('/home/student-00-4dd743e70e3f/supplier-data/descriptions/')
    sender = 'automation@example.com'
    recipient = 'student-00-4dd743e70e3f@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    now = datetime.date(datetime.now())
    report_date = now.strftime('%B %-d, %Y')
    attachment = '/tmp/processed.pdf'
    report_title = 'Processed update on'
    reports.generate_report(attachment, report_title, pdf_fruit_data(fruit_data))

    email = emails.generate_email(sender, recipient, subject, email_fruit_data(fruit_data), attachment)
    emails.send_email(email)

