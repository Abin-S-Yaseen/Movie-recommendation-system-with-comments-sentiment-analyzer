# Movie-recommendation-system-with-comments-sentiment-analyzer
 A Machine learning web application with Flask backend that recommends movies based on its similarities with a movie that you entered. It is also capable of doing sentiment analysis on the movie comments using data scraped from IMDB website.
 
 Functions
 ---------
 1) Recommends new movies which are similar to the movies you enter in the search box
 2) provides an analysis of the IMDb comments of the recommended movies
 
 How to setup the project
 ------------------------
 Step 1 -> install python version 3.10.7 (other versions might work, give it a try)
 Step 2 -> locate and open the 'main' folder in the project directory
 Step 3 -> open command prompt in the main folder(by right clicking and selecting 'open in Terminal' option) and type "pip install -r requirements.txt"
 Step 4 -> python and the required libraries for this project are now installed in your pc
 Step 5 -> now open the "datasets" folder and locate the "extract datasets.zip" file. 
           Then extract the files inside it and place there(inside the datasets folder)      [Already mentioned in a text file named "Read this.txt"]
 Step 6 -> now open the "models" folder and locate the "extract models.zip" file.
           Then extract the files inside it and and place there(inside the models folder)    [Already mentioned in a text file named "Read this.txt"]
 Step 7 -> now inside the "main" folder, open the command prompt(by right clicking and selecting 'open in Terminal' option)
 Step 8 -> inside the command prompt, type "python app.py" and press Enter
 Step 9 -> locate the newly genereted flask sever link in the command prompt and paste it in any browser
 Step 10 -> Thats it, Now enjoy !!!
 
 How to use the project
 ----------------------
 Step 1 -> type a movie name in the search box letter by letter. A dropdown appears below the search box
 Step 2 -> select the movie from the dropdown and press "submit" button
 Step 3 -> top 10 most similar movies to your entered movie appears on the page
 Step 4 -> click on any of the recommended movies which opens a new page with the analysis of that movie's IMDb comments
 Step 5 -> you can see 'Top positive comments' and 'Top negative comments' of the selected movie in the newly formed webpage
 
 How it works
 ------------
 * This project has two parts
     > Movie Recommendation system
     > Movie comments sentiment analysis
     
 * Ⅰ part uses Count vectorizer and cosine similarity to predict top 10 most similar movies.
   When you enter a movie and press 'Submit button', the text is extracted from the searchbox.
   Then the text is vectorized using CountVectorizer library in python. [since the model can only understand numbers and not texts, it is necessary
                                                                          to perform text vectorization in which the text is converted to numbers]
   Then the vectorized text is passed to the Cosine Similarity model which checks the similarity score of that movie with other movies in the dataset.
   Then the top 10 movies with the highest similarity score is displayed on the webpage.
    
 * Ⅱ part uses Naive Bayes Machine Learning model to perform sentiment analysis.
   When you click on any of the recommended movies, the top 25 comments of that movie are webscraped from the IMDb website.
   Then those comments undergo data pre-processing(cleaning, stemming etc)
   Then those comments undergo Text vectorization (but here we use tf-idf[term frequency inverse document frequency] library for vectorizing)
   After vectorization, the comments are fed to a trained machine learning model(Naive bayes) which predicts if a particular comment is positive or negative.
   Then the segregated positive and negative comments are displayed on a new webpage
            
