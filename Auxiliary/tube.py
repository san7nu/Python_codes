from pytube import YouTube,Playlist
import sys

if len(sys.argv[1:]) != 1:
        print("Only one link supported")
        sys.exit()

pl = Playlist(sys.argv[1])
pl.populate_video_urls()
#print(len(pl.video_urls))

for i,vid in enumerate(pl.video_urls):
        yt = YouTube(vid)
        print("---START---",i,yt.title,yt.streams.filter(only_audio=True).first())
        stream = yt.streams.filter(only_audio=True).first()
        stream.download()
        print("---END---",i,yt.title)