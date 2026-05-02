import requests
import random

def main():
    games = load_games()
    by_genre = filter_by_genre(games, input("What genre of games do you like? "))
    if not by_genre:
        print("No games found for that genre!")
        return
    rec = recommend_games(by_genre)
    print("\nGames you might like!\n")
    for i, g in enumerate(rec, 1):
        print(f"{i}. {g['title']} (Genre: {g['genre']}, Platform: {g['platform']}, Rating: {g['rating']})")
    print()

def load_games(max_p=5,page_size=40):
    games = []
    for page in range(1, max_p+1):
        url = f"https://api.rawg.io/api/games?key=8f7fb95a71aa48499feea26587ed647a&page={page}&page_size={page_size}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["results"]

        for game in data:
            if game.get("platforms"):
                platform_names = []
                for p in game["platforms"][:3]:
                    platform_names.append(p["platform"]["name"])
                plat = ", ".join(platform_names)
            else:
                plat = "Unknown"

            games.append({
                "title": game["name"],
                "genre": game["genres"][0]["name"] if game["genres"] else "Unknown",
                "platform": plat,
                "rating": game.get("rating", 0)
            })
    return games

def filter_by_genre(games, genre):
    filtered = []
    for game in games:
        if game["genre"].lower() == genre.lower():
            filtered.append(game)
    return filtered

def recommend_games(by_genre):
    k = min(5, len(by_genre))
    rnd_list = random.sample(by_genre, k)
    return rnd_list

if __name__ == "__main__":
    main()
