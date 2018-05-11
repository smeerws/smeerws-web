convert smeerws-fua-web-*.jpg -background transparent -fill grey -font Liberation-Sans-Bold -size 140x80 -pointsize 50 -gravity southeast -annotate +0+0 'Copyright SMEERWS' -scene 1 cr-smeerws-fua.jpg

convert -density 150 input.pdf -quality 90 output.png

convert -list font|grep Liberation-Sans
