def get_playlist_info(songs: dict, n_songs: int) -> float:
    song_names = [input(f'Название {idx}-й песни: ')
                  for idx in range(1, n_songs+1)]

    total_playtime = 0
    for name in song_names:
        try:
            total_playtime += songs[name]
        except KeyError:
            print(
                f'Не нашли песню c названием "{name}", плейлист будет без неё :(')
    print(f'Общее время звучания песен: {round(total_playtime, 2)} минуты')
    return total_playtime


if __name__ == '__main__':
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]
    # По аналогии с задачей 3, дикт - более подходящая структура
    violator_songs_dict = {key: value for key, value in violator_songs}
    n_songs = int(input('Сколько песен выбрать?: '))
    get_playlist_info(violator_songs_dict, n_songs)
