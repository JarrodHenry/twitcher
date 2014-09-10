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

    count = 0
    for result in active:
        print("{0}-{1}: {2}".format(count,
                                    result['channel']['name'],
                                    result['channel']['url']))
        count = count + 1

    choice = input("Please select a stream: ")
    print(choice)
    

if __name__ == '__main__':
    main()
