#!/bin/sh
for i in *.md; do
sed -i "s|./images|{filename}images|" $i
done
