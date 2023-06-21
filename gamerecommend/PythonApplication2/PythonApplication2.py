import csv
import os
import random

def read_games(file_name):
    games = []
    with open(file_name, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            games.append(row)
    return games

def filter_games(games, genre=None):
    filtered_games = []
    for game in games:
        if genre and (game['Action'].lower() == 'true' or \
                      game['Adventure'].lower() == 'true' or \
                      game['Comedy'].lower() == 'true' or \
                      game['Crime'].lower() == 'true' or \
                      game['Family'].lower() == 'true' or \
                      game['Fantasy'].lower() == 'true' or \
                      game['Mystery'].lower() == 'true' or \
                      game['Sci-Fi'].lower() == 'true' or \
                      game['Thriller'].lower() == 'true'):
            filtered_games.append(game)
    return filtered_games

def recommend_game(games):
    print("Select your favorite game genre:")
    print("1. Action")
    print("2. Adventure")
    print("3. Comedy")
    print("4. Crime")
    print("5. Family")
    print("6. Fantasy")
    print("7. Mystery")
    print("8. Sci-Fi")
    print("9. Thriller")
    genre_choice = input("Enter your choice (1-9): ")

    genre_map = {
        '1': 'Action',
        '2': 'Adventure',
        '3': 'Comedy',
        '4': 'Crime',
        '5': 'Family',
        '6': 'Fantasy',
        '7': 'Mystery',
        '8': 'Sci-Fi',
        '9': 'Thriller'
    }
    selected_genre = genre_map.get(genre_choice)

    filtered_games = filter_games(games, genre=selected_genre)

    if not filtered_games:
        print("No games found matching the criteria.")
    else:
        random_game = random.choice(filtered_games)
        print("Recommended game:")
        print("- " + random_game['name'])

# Dosya yolunu güncelleyin
file_name = "imdb-videogames.csv"
file_path = os.path.join(os.getcwd(), file_name)

games = read_games(file_path)
recommend_game(games)

