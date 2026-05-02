from project import load_games
from project import filter_by_genre
from project import recommend_games

def test_load_games():
    games = load_games(max_p=1, page_size=1)
    assert isinstance(games, list)
    assert len(games) > 0
    game = games[0]
    for key in ["title", "genre", "platform", "rating"]:
        assert key in game

def test_filter_by_genre():
    sample_games = [{"genre": "Action"}, {"genre": "Adventure"}]
    result = filter_by_genre(sample_games, "Action")
    assert result == [{"genre": "Action"}]

def test_recommend_games():
    sample_games = [
        {"title": "The Witcher 3: Wild Hunt", "genre": "RPG", "platform": "PC", "rating": 4.7},
        {"title": "Skyrim", "genre": "RPG", "platform": "PC", "rating": 4.5},
        {"title": "Dragon Age: Inquisition", "genre": "RPG", "platform": "PC", "rating": 4.2},
        {"title": "GTA v", "genre": "RPG", "platform": "PC", "rating": 4.5}
        ]
    result = recommend_games(sample_games)
    assert len(result) <= 5
    assert all(game in sample_games for game in result)
