import webbrowser


def search_web(query):

    # Create Google search URL
    google_url = (
        "https://www.google.com/search?q="
        + query.replace(" ", "+")
    )

    print("\n================================")
    print("AGENT WEB SEARCH")
    print("================================")
    print("Searching for:", query)

    # Open Google
    webbrowser.open(google_url)

    # Return search information to agent
    return {
        "query": query,
        "search_url": google_url
    }