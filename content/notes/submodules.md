Title: Starting a blog
Author: AC
Date: 2022-07-25
Tags: pelican, tutorials
Slug: working-with-submodules
Summary: How to update a submodule and the superproject

https://stackoverflow.com/questions/5814319/git-submodule-push
https://stackoverflow.com/questions/10848191/git-submodule-commit-hooks
https://dopeddude.medium.com/git-submodule-with-git-hooks-for-scalable-repos-50924f969937

I'm okay with git -- that is, I interact with it on the command line, I know what's going on at a high level, and I can (if I brace myself) do an interactive rebase. I don't have a deep understanding of it, and I mostly do basic stuff with it. This is the first time I've tried to do much with submodules, so I've been looking into getting the output (a submodule) correctly pushed and updated when I'm pushing new posts to the superproject.

One of the important parts of working with a submodule is that the submodule needs to be updated (`git add` and `git commit`) independently from the superproject. So, for example, if you're in the superproject and you do a `git add .`, it will not take care of adding the changes to the submodule, if there are any.

In the superproject's `.git/hooks/pre-push`
```
#!/bin/bash

echo "Starting pre-push"
lastcommit=`git log origin/main -1 --oneline`
echo "Last commit: ${lastcommit} ... now running make publish"
make publish
cd output && git add -A . && git commit -m "$lastcommit" && git push origin main
cd ..
echo "pwd: $(pwd)"
git submodule update --recursive
exit 0
```

Now, I can do a workflow where I write a post in the superproject's `/content` directory, and do:
``` 
git add -A .
git commit -m 'My message'
git push origin main
```
The `/output` directory gets updated and the output submodule gets pushed as part of the pre-push hook in the superproject.