# Download Youtube video using python
from pytube import YouTube

YouTube("https://www.youtube.com/watch?v=KTIl1MugsSY").streams.first().download(filename="DownByPy")