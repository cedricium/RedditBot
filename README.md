# RedditBot
## Development of a Reddit bot, written with Python and Praw 

### Goals for this project:
* Learn Python
* Create a personal "assistant" bot

### How This Project Turned Out:
* "Save and Record Links" Bot
  * When I type the command "!save - #tag" on any reddit thread, the bot:
    1. saves the title as a hyperlink with the url of the thread in a document hosted on GitHub
    2. saves my comment's id so it doesn't reply to the same comment twice
    3. runs a bash script that automatically pushes changes made to both documents to GitHub repository
    4. saved links document is a markdown document that gets saved and updated with each push to GH for my viewing later

### Resources:
* [/u/busterroni](https://www.reddit.com/user/busterroni)'s YouTube tutorial - [found here](https://www.youtube.com/watch?v=krTUf7BpTc0") 
