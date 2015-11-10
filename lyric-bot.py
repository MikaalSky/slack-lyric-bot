import random
import BaseHTTPServer

HOSTNAME = ""
PORTNUMB = 5555

# TODO (Gigabyte Giant): Move this to a JSON file
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
        "lyric": "The measure of a life is a measure of love and respect, so hard to earn, so easily burned",
        "band": "Rush",
        "song": "The Garden"
    }
]

def doJSONResponse(responseText):
    return "{\"response_type\":\"in_channel\",\"text\":\"" + responseText + "\"}"

def pickRandomLyric():
    pickedSong = lyrics[random.randrange(len(lyrics))]
    return "_" + pickedSong["lyric"] + "_ -- *" + pickedSong["band"] + ", " + pickedSong["song"] + "*"

class lyricBotHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    # TODO (Gigabyte Giant): Support POST requests

    def do_GET(self):
        print("GET request")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(doJSONResponse(pickRandomLyric()))

httpServer = BaseHTTPServer.HTTPServer((HOSTNAME, PORTNUMB), lyricBotHTTPRequestHandler)
print("HTTP Server started at " + HOSTNAME + ":" + str(PORTNUMB))
httpServer.serve_forever()