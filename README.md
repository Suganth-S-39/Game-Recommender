# Game Recommender

#### Description:

This project is my final submission for CS50P, and it’s something I had fun building — a **Game Recommender**. The idea is simple: you tell the program what genre of games you like, and it will recommend a few games back to you. To make this possible, I used the RAWG Video Games Database API, which has tons of game data like titles, genres, platforms, and ratings.

### How it works

When you run the program, it asks you to type in a game genre (like “Action,” “RPG,” “Sports,” etc.). Behind the scenes, the program fetches a bunch of games from the RAWG API. I limited it to 5 pages of results so the program doesn’t take forever, but it’s still plenty of data to work with.
After collecting the games, the program filters them by the genre you chose. If there aren’t any games that match, it just tells you straight up that nothing was found. But if there are matches, it randomly picks up to 5 games and shows them to you. Each recommendation includes the game’s title, genre, the platforms it’s available on (up to three), and its average rating.
So basically, it’s like a quick way to discover new games you might enjoy without scrolling endlessly through lists.

### Features

- Pulls real data from the RAWG API.
- Lets you filter games by genre.
- Randomizes the recommendations, so you won’t see the exact same list every time.
- Handles missing data (like if a game doesn’t have a genre or listed platform, it just says “Unknown”).

### Design choices

A couple of things I thought about while building this:
- I decided to show only the first three platforms for each game. Some games have a really long list of platforms.
- I limited the number of API pages to 5 for performance reasons. Fetching everything would be too slow, but 200 games is already more than enough variety.
- For the random picks, I used Python’s `random.sample`, which ensures you don’t get duplicate games in the list.

### Why I built this

I wanted a project that felt both personal and practical. As someone who enjoys games, I often find myself stuck wondering what to play next. So I thought, why not make a small program that can give me suggestions?, It’s not a huge or complicated, but it’s something useful, and I like that it feels like a tool I could actually use.
