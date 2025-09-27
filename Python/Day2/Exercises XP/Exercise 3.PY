# ex3_zara.py
def zara_example():
    """Create and modify the Zara brand dictionary as requested."""
    brand = {
        "name": "Zara",
        "creation_date": 1975,
        "creator_name": "Amancio Ortega Gaona",
        "type_of_clothes": ["men", "women", "children", "home"],
        "international_competitors": ["Gap", "H&M", "Benetton"],
        "number_stores": 7000,
        "major_color": {
            "France": "blue",
            "Spain": "red",
            "US": ["pink", "green"]
        }
    }

    # 2. Change number of stores to 2
    brand["number_stores"] = 2

    # 3. Use type_of_clothes to print a sentence
    types = ", ".join(brand["type_of_clothes"])
    print(f"Zara makes clothes for: {types}.")

    # 4. Add country_creation
    brand["country_creation"] = "Spain"

    # 5. If international_competitors in dict, add Desigual
    if "international_competitors" in brand:
        brand["international_competitors"].append("Desigual")

    # 6. Delete creation_date
    if "creation_date" in brand:
        del brand["creation_date"]

    # 7. Print the last international competitor
    last_comp = brand["international_competitors"][-1]
    print("Last international competitor:", last_comp)

    # 8. Print major clothes colors in the US
    print("Major colors in the US:", brand["major_color"]["US"])

    # 9. Print amount of key value pairs (length)
    print("Number of keys in brand dict:", len(brand))

    # 10. Print the keys
    print("Keys:", list(brand.keys()))

    # 11. Create more_on_zara
    more_on_zara = {"creation_date": 1975, "number_stores": 10000}

    # 12. Add info from more_on_zara into brand (update merges)
    brand.update(more_on_zara)

    # 13. Print number_stores and explain
    print("Updated number_stores:", brand["number_stores"])
    print("Explanation: update() overwrote the previous number_stores value with the one from more_on_zara.")

    return brand

if __name__ == "__main__":
    final_brand = zara_example()
    # Print brand to inspect
    import pprint
    pprint.pprint(final_brand)
