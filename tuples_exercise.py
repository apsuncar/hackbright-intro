def convert_to_seconds(hours, minutes, seconds):
	hours_to_seconds = hours * 3600
	minutes_to_seconds = minutes * 60
	print seconds + hours_to_seconds + minutes_to_seconds

convert_to_seconds(0, 0, 60)

def convert_to_hours(seconds):
	