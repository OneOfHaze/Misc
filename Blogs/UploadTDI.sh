cd ./tdi.online_jekyll
jekyll build
git add .
git commit -m "New post"
git push origin
cd ..
rsync -v -rz --delete --checksum ./tdi.online_jekyll/_site/ korruptor@tdi.online:/var/www/www.tdi.online/
