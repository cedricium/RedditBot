#!/bin/bash

update = "Update docs/index.md with new saved links."

git add .
git commit -m \"$update\"
git push origin new-features
