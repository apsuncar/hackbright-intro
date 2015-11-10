test = open("april_fav_foods.txt")
test1=test.readlines()


test =open("katie_fav_foods.txt")
test2=test.readlines()


def compare_favs(x,y):
	if(x[0] == y[0]):
		print "Our fave foods are the same!"
