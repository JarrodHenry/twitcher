from twitch import TwitchTV
from logging import Logger
import shlex
import subprocess

streamers = ['joindotared', 'imaqtpie', 'riotgames', 'gaugemalamute',
             'mushisgosu', 'joindotablue']
log = Logger('twitch')
twitch = TwitchTV(log)


def main():
    active = []

    for streamer in streamers:
        x = twitch.searchStreams(streamer)
        if x:
            for stream in x:
                if stream['channel']['name'] == streamer:
                    active.append(stream)

    count = 0
    for result in active:
        print("{0} -{1}: {2}".format(count,
                                     result['channel']['name'],
                                     result['channel']['url']))
        count = count + 1

    choice = -99
    if count > 0:
        choice = input("Please select a stream: ")

    if int(choice) != -99:
        url = active[int(choice)]['channel']['url']
        command = "livestreamer --player mpv {0} high".format(url)
        subprocess.call(shlex.split(command))
    else:
        print("No active streams.\n")

if __name__ == '__main__':
    main()
