# 
# Example file for retrieving data from the internet
#
import urllib.request #instead of urllib2 like in Python 2.7


def main():
    # Open a connection to a URL using urllib2
    webUrl = urllib.request.urlopen("https://www.google.com")

    # Get the result code and print it
    print("Result code: " + str(webUrl.getcode()))

    # Read the data from the URL and print it
    data = webUrl.read()
    print(data)

if __name__ == "__main__":
    main()
