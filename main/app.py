#app.py
import pickle
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from flask import Flask, Response, render_template, request,jsonify
import json
from wtforms import StringField,Form,SubmitField,TextAreaField
 
class SearchForm(Form):
	autocomp = StringField('Enter the Movie ', id='movie_autocomplete')
	button = SubmitField("Submit")

# MOVIE RECOMMENDATION

cosine_sim = pickle.load(open('models/similarity.pickle','rb'))
movies_final = pd.read_csv('datasets/movies_final_updated.csv')

# function to clean html tags
def clean_html(text):
	clean=re.compile('<.*?>')
	return re.sub(clean, '', text)

# function to convert to lower case
def convert_lower(text):
	return text.lower()

# function to remove special characters
def remove_special(text):
	x= ''
	for i in text:
		if i.isalnum():
			x = x+i
		else:
			x = x+' '
	return x

# function for removing stopwords
def remove_stopwords(text):
	x=[]
	for i in text.split():
		if i not in stopwords.words('english'):
			x.append(i)
	y=x[:]
	x.clear()
	
	return y

# function for stemming
ps=PorterStemmer()
y=[]
def stem_words(text):
	for i in text:
		y.append(ps.stem(i))
	z=y[:]
	y.clear()
	
	return z

# join
def join(list_input):
	return " ".join(list_input)

# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(title, cosine_sim=cosine_sim):
	
	# Get the index of the movie that matches the title
	idxs = list(movies_final.loc[movies_final['title'] == title, 'index'])
	idx = idxs[0]

	# Get the pairwsie similarity scores of all movies with that movie
	sim_scores = list(enumerate(cosine_sim[idx]))

	# Sort the movies based on the similarity scores
	sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

	# Get the scores of the 10 most similar movies
	sim_scores = sim_scores[1:11]

	# Return the top 10 most similar movies
	movie_list = []
	for movies in sim_scores:
		movie_list.append(movies_final['title'].iloc[movies[0]])
	
	return movie_list

# COMMENTS ANALYSIS

tf_vect = pickle.load(open('models/tf-vect.pickle','rb'))
model = pickle.load(open('models/tf-naive-bayes.pickle','rb'))

def get_movie_comments(movie):

	reviews = []
	movie_id=list(movies_final.loc[movies_final['title'] == movie, 'imdb id'])
	page = requests.get('https://www.imdb.com/title/{}/reviews?sort=totalVotes&dir=desc&ratingFilter=0'.format(movie_id[0]))
	soup = BeautifulSoup(page.content, 'html.parser')
	movie_data=soup.find_all('div',attrs= {'class': 'lister-item-content'})

	for classes in movie_data:
		review = classes.find(class_ = 'content').text.replace('\n', '')  
		reviews.append(review)

	return reviews

def sentiment(sentence):
	sen=tf_vect.transform([sentence]).toarray()
	pred=model.predict(sen)[0]
	if pred == 1:
		return 'Positive'
	else:
		return 'negative'

def clean_comments(comments):
	comments_list = []
	for i in comments:
		i = clean_html(i)
		i = convert_lower(i)
		i = remove_special(i)
		i = remove_stopwords(i)
		i = stem_words(i)
		i = join(i)
		comments_list.append(i)

	return comments_list

movies = list(movies_final['title'])
	
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	form = SearchForm(request.form)
	return render_template("index.html", form=form)


@app.route('/recommend',methods=['POST'])
def predict():
	global my_prediction

	if request.method == 'POST':
	#	message = request.form['message']
		# vect = tf_vect.transform(data).toarray()
		form = SearchForm(request.form)
		message = form.autocomp.data
		if message in movies:
			my_prediction = get_recommendations(message)
			return render_template('index.html', form=form, prediction=my_prediction)
		else:
			return render_template('index.html', form=form, prediction=False)


@app.route('/review',methods=['POST','GET'])
def comments_analysis():
	if request.method == 'POST':
		if request.form['submit_button'] == my_prediction[0]:
			movie_name=my_prediction[0]
			comments = get_movie_comments(movie_name)
		elif request.form['submit_button'] == my_prediction[1]:
			movie_name=my_prediction[1]
			comments = get_movie_comments(movie_name)
		elif request.form['submit_button'] == my_prediction[2]:
			movie_name=my_prediction[2]
			comments = get_movie_comments(movie_name)
		elif request.form['submit_button'] == my_prediction[3]:
			movie_name=my_prediction[3]
			comments = get_movie_comments(movie_name)
		elif request.form['submit_button'] == my_prediction[4]:
			movie_name=my_prediction[4]
			comments = get_movie_comments(movie_name)
		elif request.form['submit_button'] == my_prediction[5]:
			movie_name=my_prediction[5]
			comments = get_movie_comments(movie_name)
		elif request.form['submit_button'] == my_prediction[6]:
			movie_name=my_prediction[6]
			comments = get_movie_comments(movie_name)
		elif request.form['submit_button'] == my_prediction[7]:
			movie_name=my_prediction[7]
			comments = get_movie_comments(movie_name)
		elif request.form['submit_button'] == my_prediction[8]:
			movie_name=my_prediction[8]
			comments = get_movie_comments(movie_name)
		elif request.form['submit_button'] == my_prediction[9]:
			movie_name=my_prediction[9]
			comments = get_movie_comments(movie_name)
	
	my_pred = []
	cleaned_comments = clean_comments(comments)
	for i in cleaned_comments:
		result = sentiment(i)
		my_pred.append(result)

	
	dictionary = dict(zip(comments, my_pred))
	return render_template('review.html', predictions=dictionary, movie_name=movie_name)

@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
	# movie variable defined previously  
	return Response(json.dumps(movies), mimetype='application/json')



if __name__ == '__main__':
	app.run(debug=True)
