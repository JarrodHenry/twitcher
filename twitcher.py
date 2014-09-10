from twitch import TwitchTV
from logging import Logger
from pprint import pprint

streamers = ['JoinDotaRed', 'RiotGames', 'imaqtpie']
log = Logger('twitch')
twitch = TwitchTV(log)


def main():
    active = []
    for streamer in streamers:
        x = twitch.searchStreams(streamer)
        if x:
            active.append(x[0])

    pprint(x)

if __name__ == '__main__':
    main()
