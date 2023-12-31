# reddit-migration
A simple script to assist leaving reddit whilst making some noise.

![Image example](./comments.png)

## TODO
Error handling. Raises 500 when you try to mass delete posts.

## To use
- Install `praw` and `python-dotenv` (it's in requirements.txt).
- Copy `.env.example` to `.env` and edit it as instructed.
- Run `python comments.py` to edit your comments
- Run `python textposts.py` to edit your text posts and delete the rest.
- Wait. It generally takes a few seconds per each comment.

## Why
Reddit is undergoing changes to their API. Specifically, they are [going to charge $0.24 per 1000 API requests](https://web.archive.org/web/20230614165721/https://old.reddit.com/r/reddit/comments/145bram/addressing_the_community_about_changes_to_our_api/). A paid API isn't too big of a deal, but the figure per 1000 requests is so absolutely ridiculous, it completely kills any third-party Reddit client or bot. (One popular third-party client, Apollo, was quoted [$20 million dollars to run for a year](https://web.archive.org/web/20230531221034/https://arstechnica.com/gadgets/2023/05/reddits-api-pricing-results-in-shocking-20-million-a-year-bill-for-apollo/).)

After considerable backlash from the entire community of reddit, the admins have doubled down and even (clearly falsely) alleged blackmail from the developer of Apollo. 

Because of this, Reddit is currently undergoing a mass exodus of its users, who are moving to alternatives - mostly, to the fediverse (or "Threadiverse"), via services like [Kbin](https://kbin.pub/en) and [Lemmy](https://join-lemmy.org/).

**But why edit comments?** Reddit's largest selling point is not within new posts; rather, it is in the aggregate of lots of old threads with useful information. Think: when was the last time you Googled something and found the answer in a Reddit thread? Probably not very long ago at all. Additionally, anecdotally, it appears [Reddit doesn't store edit history at all, but they do store deleted history](https://web.archive.org/web/20230614172711/https://old.reddit.com/r/help/comments/on6oky/anyway_to_view_edit_history_of_a_comment/h5ptohj/).

## Contributing
Contributions are welcome. Don't introduce any more packages.
