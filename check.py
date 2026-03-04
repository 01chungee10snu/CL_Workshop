import urllib.request
import urllib.error
try:
    urllib.request.urlopen("https://github.com/01chungee10snu/CL_Workshop")
    print("PUBLIC")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print("PRIVATE_OR_NOT_FOUND")
    else:
        print("ERROR:", e.code)
