#!/bin/bash

commit_message="Update docs/index.md with new saved links and comments replied to."

git add comments_replied_to.txt docs/index.md
git commit -m "$commit_message"
git push origin master
