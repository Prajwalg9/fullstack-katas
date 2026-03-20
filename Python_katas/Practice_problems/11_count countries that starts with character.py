from soupsieve.util import lower

Countries=['India','China','Pakistan','USA','Iran','Italy','Japan','Korea']
counter=0
print(Countries)
inp=input("Enter character to search for: ")
for country in Countries:
    if (country.lower()).startswith(inp):
        counter+=1
print(counter)