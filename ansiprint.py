
import sys
import re
import json

def ansiprint():
	colormap=[{"regex":"ip=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}","color":"32m"}]
	if len(sys.argv) >= 2:
		with open(sys.argv[1]) as f:
			colormap=json.loads(f.read())
	else:
		with open("colormap.json") as f:
			colormap=json.loads(f.read())

	for line in sys.stdin.readlines():
		for item in colormap:
			for match in re.findall(item["regex"],line):
				highlighted="\x1b["+item["color"]+match+"\x1b[0m"
				line=line.strip().replace(match,highlighted)
		print(line)

if __name__ == "__main__":
	ansiprint()

