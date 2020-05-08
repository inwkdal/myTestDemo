
def process_book(filename):
	book = open(filename)
	for line in book:
		# line in the book
		line = line.split()
		print(line)


process_book("mybook.txt")
		
