import praw
from dotenv import dotenv_values

env = dotenv_values()
client_id = env["CLIENT_ID"]
client_secret = env["CLIENT_SECRET"]
user_agent = env["USER_AGENT"]
username = env["USERNAME"]
password = env["PASSWORD"]

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

for comment in reddit.user.me().comments.new(limit=None):
    comment.edit(env["TEXT"])
    print(f"Comment edited: {comment.id}")

print("All comments edited.")
