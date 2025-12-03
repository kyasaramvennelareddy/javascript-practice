
def extract_domain(url):
    url = url.strip()

    start = url.find("://")
    if start != -1:
        url = url[start+3:]

    end = url.find("/")
    if end != -1:
        url = url[:end]

    if url.startswith("www."):
        url = url[4:]

    return url

url="https://www.info.streamforcesolutions.com"
print(extract_domain(url))


# https://www.microsoft.com
# https://www.help.microsoft.com
# https://www.info.streamforcesolutions.com/about 