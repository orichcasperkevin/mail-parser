# Importing libraries
import imaplib, email

user = 'orichcasper59@gmail.com'
password = 'lwwrsrkbpxulcgnb'
imap_url = 'imap.gmail.com'


class Mails():
	# Function to search for a key value pair
	def _search(self,key, value, con):
		result, data = con.search(None, key, '"{}"'.format(value))
		return data

	@classmethod
	def get_mails(cls,**kwargs):
		imap_url = kwargs['imap_url']
		from_email = kwargs['from']
		user = kwargs['user']
		password = kwargs['password']

		mail = imaplib.IMAP4_SSL(imap_url)
		mail.login(user, password)
		mail.select('inbox')
		data = search('FROM', 'gsmaumo@gmail.com', mail)

		mail_ids = []
		for block in data:
		    mail_ids += block.split()

		mails = []
		for i in mail_ids:
		    status, data = mail.fetch(i, '(RFC822)')
		    for response_part in data:
		        if isinstance(response_part, tuple):
		            message = email.message_from_bytes(response_part[1])
		            mail_from = message['from']
		            mail_subject = message['subject']
		            if message.is_multipart():
		                mail_content = ''

		                for part in message.get_payload():
		                    if part.get_content_type() == 'text/plain':
		                        mail_content += part.get_payload()
		            else:
		                mail_content = message.get_payload()
		            print(mail_from)
		            print(mail_subject)
		            print(mail_content)
					mails.append({
						"from":mail_from,
						"subject":mail_subject,
						"content":mail_content
					})
