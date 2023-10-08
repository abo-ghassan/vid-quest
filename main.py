# https://github.com/abo-ghassan/

from youtube_search import YoutubeSearch
import mpv
import requests.exceptions
from colorama import Fore,Style

def main():
    try:
        # Create mpv player instance
        player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True, osc=True)
        player['ytdl-format'] = 'bestvideo[height<=?240]+bestaudio/best'

        # Prompt user for search query and search for videos on YouTube
        search_query = input('Enter your search query: ')
        print(f'{Fore.YELLOW}Searching for videos...{Style.RESET_ALL}\n')
        try:
            results = YoutubeSearch(search_query, max_results=7).to_dict()
        except requests.exceptions.ConnectionError:
            print(f'{Fore.LIGHTRED_EX}Check your internet connection and try again.{Style.RESET_ALL}')
            exit()

        # Print the results
        for i, result in enumerate(results):
            print(f'{Fore.GREEN}{i}:{Style.RESET_ALL} {result["title"]}\nBy {result["channel"]} ({result["duration"]})\n')

        # Prompt user to choose a video to play
        while True:
            try:
                choice = int(input('Enter the number of the video you want to play: '))
                if choice not in range(0, 7):
                    raise ValueError
                break
            except ValueError:
                print(f'{Fore.LIGHTRED_EX}Please enter a valid number.\n{Style.RESET_ALL}')

        # Play chosen video
        youtube_url = f'https://youtube.com/watch?v={results[choice]["id"]}'
        print(f'\nPlaying "{results[choice]["title"]}"\nPlease wait...')
        player.play(youtube_url)
        player.wait_for_playback()

        # Delete player instance
        del player
    except KeyboardInterrupt:
        print(f'\n{Fore.LIGHTRED_EX}Exiting...{Style.RESET_ALL}')

if __name__ == '__main__':
    main()
