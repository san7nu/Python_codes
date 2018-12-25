from pytube import YouTube,Playlist
import sys
import multiprocessing.dummy as mp

def dload_vid(vid):
	try:
		yt=YouTube(vid)
		if yt.streams.get_by_itag('251') is not None:
			print("-----START----",yt.title,"---251---")
			stream = yt.streams.get_by_itag('251')
			stream.download()
			print("-----END----",yt.title,"---251---")
		else:
			print("-----START----",yt.title,"---140---")
			stream = yt.streams.get_by_itag('140')
			stream.download()
			print("-----END----",yt.title,"---140---")
	except Exception:
		pass

if __name__ == "__main__":
	if len(sys.argv[1:]) != 1:
			print("Only one link supported")
			sys.exit()

	pl = Playlist(sys.argv[1])
	pl.populate_video_urls()

	p=mp.Pool(100)
	p.map(dload_vid,[i for i in pl.video_urls])
	p.close()
	p.join()

