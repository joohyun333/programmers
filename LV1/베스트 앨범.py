from queue import PriorityQueue


def solution(genres, plays):
    albums = {}
    album_list = {}
    answer = []
    genres_set = set(genres)
    for i in genres_set:
        album_list[i] = PriorityQueue()
        albums[i] = 0
    for i in enumerate(zip(genres, plays)):
        genre = i[1][0]
        view = i[1][1]
        albums[genre] += view
        album_list[genre].put((-view, i[0]))
    albums = sorted(albums.items(),  key=lambda x: x[1], reverse=True)
    for i in albums:
        album = album_list.get(i[0])
        result_count = 0
        while not album.empty() and result_count != 2:
            result_count += 1
            answer.append(album.get()[1])
    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "classic", "pop"]
    plays = [500, 600, 150, 900, 800, 2500]
    print(solution(genres, plays))
