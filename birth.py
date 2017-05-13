months = ['January',
	  'February',
	  'March',
	  'April',
	  'May',
	  'June',
	  'July',
	  'August',
	  'September',
	  'October',
	  'November',
	  'December']
lst = ['st','nd','rd'] + 17*['th'] + ['st','nd','rd'] + 7*['th'] + ['st']
Day = input('Enter your birth day:\n' )
month = input('Enter your birth month:\n ')
Age = input('Enter your age:\n ')
import datetime
G= datetime.date.today().strftime("%Y")
Year = int(G) - int(Age)
mydate = datetime.date(int(Year),int(month),int(Day))
a = int(Day) - 1
b = int(month) - 1
print(mydate.strftime("%A-%d"),lst[int(a)],months[int(b)],int(Year))
