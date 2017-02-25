#!/bin/bash

commit_message="Update docs/index.md with new saved links."

git add docs/index.md
git commit -m "$commit_message"
git push origin master
