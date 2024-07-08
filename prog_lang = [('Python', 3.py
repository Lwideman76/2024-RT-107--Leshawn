prog_lang = [('Python', 3.8), ('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]

# Sort the list by version in ascending order
sorted_by_version = sorted(prog_lang, key=lambda x: x[1])

# Sort the list by length of language name in descending order
sorted_by_name_length = sorted(prog_lang, key=lambda x: len(x[0]), reverse=True)

# Filter the list to only contain languages with 'a' in the name
filtered_by_contains_a = [lang for lang in prog_lang if 'a' in lang[0].lower()]

# Filter the list to only contain languages with integer versions
filtered_by_integer_version = [lang for lang in prog_lang if isinstance(lang[1], int)]

print("Sorted by version (ascending):", sorted_by_version)
print("Sorted by name length (descending):", sorted_by_name_length)
print("Filtered by containing 'a':", filtered_by_contains_a)
print("Filtered by integer version:", filtered_by_integer_version)
