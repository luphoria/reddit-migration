import praw

client_id = '<CLIENT_ID>'
client_secret = '<CLIENT_SECRET>'
user_agent = '<USER_AGENT>'
username = '<USERNAME>'
password = '<PASSWORD>'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

new_comment_text = "Goodbye reddit"

for comment in reddit.user.me().comments.new(limit=None):
    comment.edit(new_comment_text)
    print(f"Comment edited: {comment.id}")

print("All comments edited.")
