import wikipedia
from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)

app.config.update(dict(
	DEBUG=False,
	SECRET_KEY='000000'
))

@app.route('/', methods=['GET', 'POST'])
def wiki_search():
	summary = None
	if request.method == 'POST':
		try:
			summary = wikipedia.page(title=request.form['search_title']).summary
		except wikipedia.exceptions.DisambiguationError, e:
			first_refer = e.options[0]
			summary = wikipedia.page(title=first_refer).summary
		except wikipedia.exceptions.PageError:
			summary = "Sorry. No Wikipedia pages match."
		except wikipedia.exceptions.HTTPTimeoutError:
			summary = "Sorry. Time out."
		except wikipedia.exceptions.WikipediaException:
			summary = "Sorry. An error occurs. Please try again."
	return render_template('wiki_search.html', summary=summary)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=6789)