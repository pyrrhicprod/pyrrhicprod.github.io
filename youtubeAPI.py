import urllib.request
import json

class Video():
    def __init__(self, id):
        self.id = id
        urlstring = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+ self.id +"&key=AIzaSyC_cpeKpnQ3rP5yLQ5vH21xt3FjGMQgfk8"
        with urllib.request.urlopen(urlstring) as url:
            data = json.loads(url.read().decode())

        stats = data['items'][0]['statistics']
        self.views = stats['viewCount']
        self.likes = stats['likeCount']
        self.dislikes = stats['dislikeCount']
        self.commentCount = stats['commentCount']
