# ansiprint
Reads from stdin and colorizes regex patterns using ansi codes

Edit the `colormap.json` file or create your own for specific outputs.

## Usage

```
echo ip=1.2.3.4 | python ansiprint.py
cat /var/log/messages | python ansiprint.py myformat.json
```
