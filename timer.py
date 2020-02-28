import time 
import emoji

for i in range(1, 9):
	print(emoji.emojize(":clock" + str(i) + ":", use_aliases = True))
	time.sleep(1)