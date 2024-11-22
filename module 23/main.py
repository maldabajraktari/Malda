from fastapi import FastAPI

import database
import models

app=FastAPI()

@app.got("/")
def read_root():
    return {"message": "Welcome to the Movies CRUD API"}
@app.post("/movies/",response_model=models.Movie)
def create_movie(movie: models.MovieCreate):
    movie_id=database.create_movie(movie)
    return models.Movie(id=movie_id, **movie.dict())
@app.get("/movies/", response_model=List[models.Movie])
def read_movies():
    return database.read_movies()
@app.get("/movies/",response_model=models.Movie)
def read_movie(movie_id:int
    movie=database.create_movie()