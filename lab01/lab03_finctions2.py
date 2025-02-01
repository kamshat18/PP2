# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1.Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def high_rating(movie):
    return movie["imdb"] > 5.5
#2.Write a function that returns a sublist of movies with an IMDB score above 5.5.
def imbd_score(movie_lst):
    return [movie for movie in movie_lst if movie["imdb"] > 5.5]
#3.Write a function that takes a category name and returns just those movies under that category.
def category1(movie_lst,category):
    return [movie for movie in movie_lst if ["category"]==category]
#4.Write a function that takes a list of movies and computes the average IMDB score.
def average(movie_lst):
    if not movie_lst:
        return 0
    return sum(movie["imdb"] for movie in movie_lst) / len(movie_lst)
#5.Write a function that takes a category and computes the average IMDB score.
def average_by_category(movie_list, category):
    filtered_movies = category1(movie_list, category)  # Теперь правильно
    return average(filtered_movies)

print(high_rating(movies[1]))
print(imbd_score(movies))
print(category1(movies,"Romance"))
print(average(movies))
print(average_by_category(movies, "Suspense"))