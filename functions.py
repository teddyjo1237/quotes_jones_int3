def display_quotes(quotes, count):
    if count >= len(quotes):
        print("All Quotes:")
        view_quotes(quotes)
    else:
        print(f"First {count} Quotes:")
        for i in range(count):
            print_quote(quotes[i])