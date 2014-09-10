from twitch import TwitchTV
from logging import Logger


streamers = ['JoinDotaRed', 'RiotGames', 'imaqtpie']
log = Logger('twitch')
twitch = TwitchTV(log)


def main():
    active = []
    count = 0
    for streamer in streamers:
        x = twitch.searchStreams(streamer)
        if x:
            if x[count]['channel']['name'] is streamer:
                active.append(x[count])
                count = count + 1

    for result in x:
        print("{0}: {1}".format(result['channel']['name'],
                                result['channel']['url']))

if __name__ == '__main__':
    main()
