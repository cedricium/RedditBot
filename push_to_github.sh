#!/bin/bash

commit_message="Update docs/index.md with new saved links."

git add .
git commit -m "$commit_message"
git push origin new-features
