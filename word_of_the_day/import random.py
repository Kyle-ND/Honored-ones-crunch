import random

def get_random_quote(file_path):
    try:
        with open(file_path, 'r') as file:
            quotes = file.readlines()
        
        # Strip newline characters from each quote
        quotes = [quote.strip() for quote in quotes if quote.strip()]
        
        if not quotes:
            return "No quotes found."

        return random.choice(quotes)
    
    except FileNotFoundError:
        return "The file was not found."

# Example usage
quote = get_random_quote('quotes.txt')
print(quote)
