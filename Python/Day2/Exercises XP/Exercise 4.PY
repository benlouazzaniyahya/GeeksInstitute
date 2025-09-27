# ex4_describe_city.py
def describe_city(city: str, country: str = "Iceland") -> None:
    """Print 'city is in country' with the provided values."""
    print(f"{city} is in {country}.")

if __name__ == "__main__":
    describe_city("Reykjavik")          # uses default country
    describe_city("Paris", "France")    # explicit country
