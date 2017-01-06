cd ./triple-aye_jekyll/
jekyll build
git add .
git commit -m "New post"
git push origin
cd ..
cp -r ./triple-aye_jekyll/_site/* ./github.io/
cd github.io/
git add .
git commit -m "Updating mirror"
git push origin

