import random
import BaseHTTPServer

HOSTNAME = "0.0.0.0"
PORTNUMB = 5555

lyricFile = "./lyrics.txt"

lyrics = []

def doJSONResponse(responseText):
    return "{\"response_type\":\"in_channel\",\"text\":\"" + responseText + "\"}"

def pickRandomLyric():
    pickedSong = lyrics[random.randrange(len(lyrics))]
    return str(pickedSong)

class lyricBotHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    # TODO (Gigabyte Giant): Support POST requests

    def do_GET(self):
        print("GET request")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(doJSONResponse(pickRandomLyric()))

print("Initializing lyrics file")

for ln in open(lyricFile, "r"):
    lyrics.append(ln)

print("Loaded " + str(len(lyrics)) + " song lyrics!")

httpServer = BaseHTTPServer.HTTPServer((HOSTNAME, PORTNUMB), lyricBotHTTPRequestHandler)
print("HTTP Server started at " + HOSTNAME + ":" + str(PORTNUMB))
httpServer.serve_forever()