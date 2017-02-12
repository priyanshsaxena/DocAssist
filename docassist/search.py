from googlea import search
from get_url_data import getFromURL
import summarize
def main(disease):
	results = search(disease+" symptoms treatment",stop=5)
	ctr = 0
	ret = []
	for i in results:
		ctr += 1
		if(ctr==4):
			break
		article = getFromURL(str(i))
		# print article.cleaned_text
		# print ">>>>>>>>>>>>>>>>>>>Summary"
		summ =  summarize.summarize_text(article.cleaned_text)
		ret.append("\n==================================================================================\n\t\tTitle: " + article.title + "\n-\n\t\tSummary\n" + " ".join(summ.summaries) + "\n-\n\t\tImage: " + article.top_image.get_src())
	# file = open("/home/priyansh/Out.txt","w")
	# for i in ret:
		# file.write("\n")
		# file.write("------------------------------------------------------------------------------------")
	# 	# file.write("Title:\t"+i[0])
	# 	# file.write("\n")
	# 	# file.write("Summary:\t"+i[1])
	# 	# file.write(" "(summ))
		# if(len(i)>10):
			# file.write(str(i))
	return "  ".join(ret)

if __name__ == '__main__':
	main()