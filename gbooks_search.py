import requests

def gbooks_search(search_terms):
	#Replaces any spaces in the search terms with +'s following the url format
	search_terms = search_terms.replace(' ', '+')
	url = "https://www.googleapis.com/books/v1/volumes?q=" + search_terms
	results = requests.get(url)
	#Returns a json of the results of the get request
	content = results.json()
	try:
		data = content['items']
	except:
		#If there is no data end the script, and prompt user for restart
		print('No Data')
		check_restart()

	title = []
	images = []
	pages =[]
	author = []

	#Some books lack certain fields
	#If they do replace the field w/ N/A so not to return an error
	for book in data:
		try:
			new = (book['volumeInfo'])
		except:
			print('No Data')
			start()
		try:
			title.append(new['title'])
		except:
			title.append('N/A')
		try:
			pages.append(new['pageCount'])
		except:
			pages.append('N/A')
		try:
			author.append(new['authors'])
		except:
			author.append('N/A')
		try:
			image_url = (new['imageLinks'])
			image = (image_url['thumbnail'])
			images.append(image)
		except:
			images.append('N/A')

	#Google books search returns 10 results
	#Loop the results, and print on separate lines
	#If there are fewer than 10 titles in the list end the loop
	x = 0
	while x < 10:
		try:
			print('Book Title: ' + title[x])
		except IndexError:
			break
		print('AuthorList:')
		print(author[x])
		print('ImgUrl: ' + images[x])
		print('Page Count: ' + str(pages[x]))
		print('\n')
		x += 1

#Function to check if the user would like to make another search or exit
def check_restart():
	while True:
		yn = input('Restart? (y/n):').lower()
		if yn == 'y':
			return start()
		elif yn == 'n':
			return False
		else:
			True

#Main function to start the search
def start():
	search_terms = input("Enter a book to search for: ")
	print('\n' + "Book List" + '\n')
	gbooks_search(search_terms)
	check_restart()


#Runs the script
start()