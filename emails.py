import random

def get_email_total(service):
    labels = service.users().labels().list(userId='me').execute()['labels']

    CAC_label_id = None
    for label in labels:
        if label['name'] == 'CAC':
            CAC_label_id = label['id']
    CAC_label_info = service.users().labels().get(userId='me', id=CAC_label_id).execute()
    number_of_emails = CAC_label_info['messagesTotal']
    return number_of_emails


def get_email_snippet(service):
    email_list = service.users().messages().list(userId='me', q='Meditations@cac.org').execute()
    email_messages = email_list['messages']

    while email_list.get('nextPageToken'):
        next_page_token = email_list['nextPageToken']
        email_list = service.users().messages().list(userId='me', q='Meditations@cac.org', pageToken=next_page_token).execute()
        email_messages = email_messages + email_list['messages']

    random_number = random.randint(0, get_email_total(service))
    specific_email = email_messages[random_number]
    email_id = specific_email['id']
    email_message = service.users().messages().get(userId='me', id=email_id).execute()
    snippet = email_message['snippet'].encode('ascii', 'ignore').decode().strip()
    print('snippet:', snippet)
    return snippet