from queue import PriorityQueue
def solution(genres, plays):
    albums = {}
    albums_list = PriorityQueue()
    genres_set = set(genres)
    


    for i in enumerate(zip(genres, plays)):
        genre = i[1][0]
        view = i[1][1]
        if albums.get(genre):
            albums[genre] += view
            albums_list.put((view, genre, i[0]))
        else:
            albums[genre] = view
            albums_list.put((view, genre, i[0]))
    return genres_set


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))
