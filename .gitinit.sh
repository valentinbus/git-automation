
cd /Users/valentinbus/Documents/repo/$1
git init
git remote add origin git@github.com:valentinbus/$1.git
touch README.md
git add .
git commit -m "Initial commit"
git push -u origin master
