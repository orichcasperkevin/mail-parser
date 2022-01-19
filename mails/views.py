from datetime import datetime
from dateutil import parser

from django.shortcuts import render
from django.http import HttpResponse
from mails.models import Mail

import mailparser
# create a function
def index(request):
	# create a dictionary to pass
	# data to the template
	mails = Mail.objects.all()
	context ={
	    "mails": mails
	}
	# return response with template and context
	return render(request, "index.html", context)

def upload(request):
	if request.method == 'POST':
		file = request.FILES['file'].read()

		#extracting file content.
		parsed_dict = {}
		mail = mailparser.parse_from_bytes(file)
		text_plain = mail.text_plain
		text_plain_items = text_plain[0].split("\n")
		for item in text_plain_items:
			pairs = item.split(':')
			if len(pairs) > 1:
				# merge all items from the second item.
				item = ":".join(pairs[1:])
				field = pairs[0].replace("*",'')
				value = item.replace("*",'')

				parsed_dict[str(field)] = value

	save_to_database(parsed_dict)
	return HttpResponse(status=201)

def save_to_database(parsed_dict):
	print(parsed_dict)
	#input this into database.
	#first format the date(s).
	date = parsed_dict['Date']
	date = parser.parse(date)
	#pickup date
	pickup_date = parsed_dict['Pickup']
	pickup_date = parser.parse(pickup_date)
	#delivery date
	delivery_date = parsed_dict['Delivery']
	delivery_date = parser.parse(delivery_date)
	#A tricky parsing happened with from, we have to extarct to again
	from_ = parsed_dict['# From']
	from_to = from_.split(":")
	from_ = from_to[0]
	from_ = from_.replace('To','')
	to = from_to[1]

	new_mail = Mail.objects.create(
		date = date,
		source_email = parsed_dict['From'],
		pro_number = parsed_dict['PRO Number'],
		loaded_miles = parsed_dict['Loaded Miles'],
		pickup = pickup_date,
		delivery = delivery_date,
		no_of_additional_stops = parsed_dict['Number of Additional Stops'],
		vehicle_size = parsed_dict['Vehicle Size'],
		commodity = parsed_dict['Commodity'],
		max_pieces = parsed_dict['Maximum Pieces'],
		max_weight = parsed_dict['Maximum Weight'],
		from_address = from_,
		to_address = to,
		dimensions = parsed_dict['Â\xa0Â\xa0Â\xa0Â\xa0Dimensions'],
		stackable = parsed_dict['Â\xa0Â\xa0Â\xa0Â\xa0Stackable'],
	)
	new_mail.save()
