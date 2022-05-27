import pyshorteners
url=input("enter url:")
s=pyshorteners.Shortener().tinyurl.short(url)
print("your shorted is:",s)