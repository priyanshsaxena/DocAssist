from goose import Goose


def main():
	pass
def getFromURL(url):
	'''
	returns object which has all data 
	'''
	g = Goose()
	article = g.extract(url=url)
	# >>> article.title
	# u'Las listas de espera se agravan'
	# >>> article.cleaned_text[:150]
	return article

if __name__ == '__main__':
	main()