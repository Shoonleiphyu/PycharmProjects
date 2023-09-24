import wikipedia

while True:
    # Prompt the user for input
    user_input = input("Enter a page title or search phrase (blank to exit): ")

    # Check if user wants to exit
    if not user_input:
        break

    try:
        # Get the Wikipedia page
        page = wikipedia.page(user_input, auto_suggest=False)

        # Print the title, summary, and URL
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")

    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation error
        print(f"DisambiguationError: {e.options}")

    except wikipedia.exceptions.HTTPTimeoutError as e:
        # Handle HTTP timeout error
        print(f"HTTPTimeoutError: {e}")

    except wikipedia.exceptions.WikipediaException as e:
        # Handle other Wikipedia exceptions
        print(f"WikipediaException: {e}")

    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
