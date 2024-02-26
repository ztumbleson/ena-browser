import requests

enaBrowserBaseUrl = "https://www.ebi.ac.uk/ena/browser/api/"
enaBrowserXML = "xml"

queryUrl = enaBrowserBaseUrl + "xml/search?" + "result=sample&limit=10"
response = requests.get(queryUrl)

if response.status_code == 200:
    print("Success! Results:")
    print(response)
    print(response.text)
elif response.status_code == 404:
    print("Invalid URL, please check formatting code and try again:\n")
    print("Failing URL: " + queryUrl)
elif response.status_code == 500 or response.status_code == 400:
    print("Server Error Occurred")
    print("Server Message: \n\n" + response.text)