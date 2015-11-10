import random
import BaseHTTPServer

# Song lyrics are (sometimes) inspirational...

lyrics = [
	{
		"lyric": "If you choose not to decide, you still have made a choice",
		"band": "Rush",
		"song": "Freewill"
	},
	{
		"lyric": "All that you can do is wish them well",
		"band": "Rush",
		"song": "Wish them well"
	},
	{
		"lyric": "The measure of a life is a measure of love and respect, so hard to earn so easily burned",
		"band": "Rush",
		"song": "The Garden"
	}
]

def pickSongLogic():
	pickedSong = lyrics[random.randrange(len(lyrics))]
	writeStr = "_" + pickedSong["lyric"] + "_ -- *" + pickedSong["band"] + ", " + pickedSong["song"] + "*"

	return "{\"response_type\":\"in_channel\",\"text\":\"" + writeStr + "\"}"

class gigaHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_POST(self):
		print("POST")
		print(self.request)
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers()

		self.wfile.write(pickSongLogic)

	def do_GET(self):
		print(self.request)
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers()

		self.wfile.write(pickSongLogic)

httpd = BaseHTTPServer.HTTPServer(("107.191.102.11", 5555), gigaHTTPRequestHandler)
httpd.serve_forever()
