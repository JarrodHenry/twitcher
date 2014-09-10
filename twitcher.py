from twitch import TwitchTV
from logging import Logger


streamers = ['joindotared', 'imaqtpie', 'riotgames']
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

    for result in active:
        print("{0}: {1}".format(result['channel']['name'],
                                result['channel']['url']))

if __name__ == '__main__':
    main()
