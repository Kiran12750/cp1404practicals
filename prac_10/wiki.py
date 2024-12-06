import wikipedia


def get_wikipedia_page():
    title = input("Enter page title: ")

    # Continue only if the title is not empty
    while title != "":
        try:
            # Use search() without autosuggest argument
            search_results = wikipedia.search(title)

            if not search_results:
                print(f'Page id "{title}" does not match any pages. Try another id!')
            else:
                # Take the first result from the search
                page_title = search_results[0]
                page = wikipedia.page(page_title)

                print(
                    f"\n{page.title}\n{page.summary[:500]}...")  # Print the title and the first 500 characters of the summary
                print(f"URL: {page.url}\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print(f"We need a more specific title. Try one of the following:\n{e.options}")

        except wikipedia.exceptions.PageError:
            print(f"Page id '{title}' does not match any pages. Try another id!")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Ask for another title after the current one has been processed
        title = input("Enter page title: ")

    print("Thank you.")


# Call the function to start
get_wikipedia_page()
