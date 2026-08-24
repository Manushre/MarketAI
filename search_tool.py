from urllib.parse import quote


def search_web(query):

    google_url = (
        "https://www.google.com/search?q="
        + quote(query)
    )

    print("\n================================")
    print("AGENT WEB SEARCH")
    print("================================")
    print("Searching for:", query)

    return {
        "query": query,
        "search_url": google_url
    }