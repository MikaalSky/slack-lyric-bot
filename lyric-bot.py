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
	}
]

class gigaHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		print(self.request)
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers()
	
		pickedSong = lyrics[random.randrange(len(lyrics))]

		writeStr = pickedSong["lyric"] + " -- " + pickedSong["band"] + ", " + pickedSong["song"]

		self.wfile.write("{\"response_type\":\"in_channel\",\"text\":\"" + writeStr + "\"}")

httpd = BaseHTTPServer.HTTPServer(("107.191.102.11", 5555), gigaHTTPRequestHandler)
httpd.serve_forever()
