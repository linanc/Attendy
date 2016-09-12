import facebook
import csv

#update token; 2 hr expiry : https://developers.facebook.com/tools/explorer/
token = 'EAACEdEose0cBAIxkLtzrcoFQZAUK5bIPx8HowmCzo3B6jcoGBZBKrDjWylK4xo2bbTXYjqkDUwIZB2qQJZCrrGUQRjI0ejRhzQz5wQs6Pj93J2DkVptsyZBFCzpLZB03rtk08qHMw5eiZBxvKX9zvZCXBROVTOV1G3QfZBYf0krD4mgZDZD'
# IEOR 171 Facebook Group ID
group_id = '1061878383932263' 

graph = facebook.GraphAPI(access_token=token, version='2.7')
# GET events in group
group_obj = graph.get_object(id=group_id, fields='events')

# Create event id to date dictionary
event_dates = dict()
for i in group_obj['events']['data']:
	event_id = i['id']
	date_str = i['start_time'].split('T')[0]
	event_dates[event_id] = date_str

# Create date to names dictionary 
attendance = dict()
for event in event_dates:
	attendance[event_dates[event]] = set()
	# GET tags of photos in event
	event_obj = graph.get_object(id=event + '/photos?', fields='tags')
	# need to test if multiple photos per event works
	tags = event_obj['data'][0]['tags']['data']
	for tag in tags:
		attendance[event_dates[event]].add(tag['name'])

all_students = set()
for date in attendance:
	for name in attendance[date]:
		all_students.add(name)

first_row = ['IEOR 171', 'Attendance']
date_row = [''] + [date for date in sorted(event_dates.values())]
f = '171_attendy.csv'
with open(f, 'wt', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(first_row)
	writer.writerow(date_row)
	attendance_dates = sorted(event_dates.values())
	for student in sorted(all_students):
		row = [student]
		for date in attendance_dates:
			if student in attendance[date]:
				row.append('1')
			else:
				row.append('')
		writer.writerow(row)