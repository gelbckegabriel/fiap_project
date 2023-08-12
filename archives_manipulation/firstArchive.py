"""
FOR 'OPEN' YOU CAN USE:
r - Read.
w - Write.
a - Append (Read and Write, most used for Logs).
x - Exclusive (You'll open and manipulate, and nothing else will be able to use it while you're using).
"""

archive = open("first_archive.txt", "w")

archive.write("Hello, World!")
archive.close()

# USING 'WITH', IT CLOSES THE FILE AUTOMATICALLY, WITHOUT THE NEED OF USING archive.close()
#with open("first_archive.txt", "a") as archive:
#    archive.write("\nGabriel Gelbcke!")

with open("first_archive.txt", "r") as archive:
    content = archive.read()

print(content)
