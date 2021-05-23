from pytube import YouTube


url = input("enter the url here -> ")## the url from the web browser$

ytd = YouTube(url).streams.first().download() ## here we download it$

print("download is successfull") ## some prints$





