import googleapiclient.discovery

class FirstComment:
    def __init__(self):
        KEY = 'KEY HERE'
        self.youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey = KEY)

    def get_last_comment(self, youtube, id, token=''):
        response = youtube.commentThreads().list(part='snippet', pageToken=token, videoId=id, textFormat='plainText', maxResults=100).execute()
        if 'nextPageToken' in response:
            return self.get_last_comment(youtube, id, response['nextPageToken'])
        comment = response['items'][-1]['snippet']['topLevelComment']['snippet']
        comment_data = {
            'text' : comment['textDisplay'],
            'name' : comment['authorDisplayName'],
            'photo_url' : comment['authorProfileImageUrl'],
            'date' : comment['publishedAt'][:10] + ' at ' + comment['publishedAt'][11:-1]
        }
        return comment_data

if __name__ == "__main__":
    link = input('Enter video link')
    c = FirstComment()
    print(c.get_last_comment(c.youtube, link[link.index('?v=') + 3:]))
