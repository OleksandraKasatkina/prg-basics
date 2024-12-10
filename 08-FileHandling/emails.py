import re

def email_sender(email_content):
    """Extracts the sender's email address from the email."""
    match = re.search(r"From:.*<(.+?)>", email_content)
    return match.group(1) if match else None

def email_recipient(email_content):
    """Extracts the recipient's email address from the email."""
    match = re.search(r"To:.*<(.+?)>", email_content)
    return match.group(1) if match else None

def email_subject(email_content):
    """Extracts the email subject."""
    match = re.search(r"Subject: (.+)", email_content)
    return match.group(1) if match else None

def email_body(email_content):
    """Extracts the body of the email."""
    # Split content into headers and body by the first blank line
    parts = email_content.split("\n\n", 1)
    return parts[1].strip() if len(parts) > 1 else None