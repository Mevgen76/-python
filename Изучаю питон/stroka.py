word = "eating, sleeping, pissing"
hobby = word.split(', ')

result = ", ".join(h.capitalize() for h in hobby)
print(result)