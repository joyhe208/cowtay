Just when you thought cowsay couldn't get any sillier...
<br>

Current functionality:
cowtay pipes a random lyric from a user-inputed Taylor Swift album/song into cowsay.

To implement:
- Random lyric generation with no input from stdin or the command-line. Currently, if no command-line argument is given, the script will assume stdin isn't empty and will try to read from it. If stdin is empty, though, the script will hang as it does not encounter an EOF.
- All the fun cowsay flags. This shouldn't be too hard to implement – I'm just lazy.
