# Movie-recommendation-system-with-comments-sentiment-analyzer
 A Machine learning web application with Flask backend that recommends movies based on its similarities with a movie that you entered. It is also capable of doing sentiment analysis on the movie comments using data scraped from IMDB website.
 
 Functions
 ---------
 1) Recommends new movies which are similar to the movies you enter in the search box <br>
 2) provides an analysis of the IMDb comments of the recommended movies <br>
 
 
 How to setup the project
 ------------------------
 **Step 1** -> Install python version 3.10.7 (other versions might work, give it a try) <br>
 
 **Step 2** -> Locate and open the 'main' folder in the project directory  <br>
 
 **Step 3** -> Open command prompt in the main folder(by right clicking and selecting 'open in Terminal' option) and type "pip install -r requirements.txt"  <br>
 
 **Step 4** -> Python and the required libraries for this project are now installed in your pc  <br>
 
 **Step 5** -> Now open the "datasets" folder and locate the "extract datasets.zip" file.   <br>
           Then extract the files inside it and place there(inside the datasets folder)      [Already mentioned in a text file named "Read this.txt"]  <br>
           
 **Step 6** -> Now open the "models" folder and locate the "extract models.zip" file.  <br>
           Then extract the files inside it and and place there(inside the models folder)    [Already mentioned in a text file named "Read this.txt"]  <br>
           
 **Step 7** -> Now inside the "main" folder, open the command prompt(by right clicking and selecting 'open in Terminal' option)  <br>
 
 **Step 8** -> Inside the command prompt, type "python app.py" and press Enter  <br>
 
 **Step 9** -> Locate the newly genereted flask sever link in the command prompt and paste it in any browser  <br>
 
 **Step 10** -> Thats it, Now enjoy !!!  <br>
 
 
 How to use the project
 ----------------------
 **Step 1** -> Type a movie name in the search box letter by letter. A dropdown appears below the search box  <br>
 
 **Step 2** -> Select the movie from the dropdown and press "submit" button  <br>
 
 **Step 3** -> Top 10 most similar movies to your entered movie appears on the page  <br>
 
 **Step 4** -> Click on any of the recommended movies which opens a new page with the analysis of that movie's IMDb comments  <br>
 
 **Step 5** -> You can see 'Top positive comments' and 'Top negative comments' of the selected movie in the newly formed webpage  <br>
 
 
 How it works
 ------------
 * This project has two parts
     1) **Movie Recommendation system**  <br>
     2) **Movie comments sentiment analysis**  <br>
     
 * Ⅰ part uses Count vectorizer and cosine similarity to predict top 10 most similar movies.  <br>
   When you enter a movie and press 'Submit button', the text is extracted from the searchbox.  <br>
   Then the text is vectorized using CountVectorizer library in python. [since the model can only understand numbers and not texts, it is necessary
                                                                          to perform text vectorization in which the text is converted to numbers]  <br>
   Then the vectorized text is passed to the Cosine Similarity model which checks the similarity score of that movie with other movies in the dataset.
   Then the top 10 movies with the highest similarity score is displayed on the webpage.  <br>
    
 * Ⅱ part uses Naive Bayes Machine Learning model to perform sentiment analysis.  <br>
   When you click on any of the recommended movies, the top 25 comments of that movie are webscraped from the IMDb website.  <br>
   Then those comments undergo data pre-processing(cleaning, stemming etc)  <br>
   Then those comments undergo Text vectorization (but here we use tf-idf[term frequency inverse document frequency] library for vectorizing)  <br>
   After vectorization, the comments are fed to a trained machine learning model(Naive bayes) which predicts if a particular comment is positive or negative.  <br>
   Then the segregated positive and negative comments are displayed on a new webpage.  <br>
            
