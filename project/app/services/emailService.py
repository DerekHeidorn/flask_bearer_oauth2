
import smtplib

from project.app.services import commonService


def _get_smtp_info():
    smtp_info = commonService.get_config_by_key('app.smtp')
    splitted_smtp = smtp_info.split(":")
    return {'host': splitted_smtp[0], 'port': int(splitted_smtp[1])}


def _send_email_msg(msg):
    smtp_info = _get_smtp_info()

    # Send the message via local SMTP server.
    with smtplib.SMTP(smtp_info['host'], smtp_info['port']) as s:
        s.send_message(msg)
