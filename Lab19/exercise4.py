# Create a set of elements called vowels with the vowels from English alphabet.
# Create a set of elements called consonants with the consonants from the
# English alphabet.
# Create a set called alpha with the union of the above two sets.
# Create another set numeric with the digits {‘0’,’1’,’2’,....’9’}
# Create a set alphanumeric with the union of digits and alpha.
# Find the difference between the sets alpha and vowels - check the difference
# between the output and the set consonants
# Find the intersection of vowels and consonants, vowels and alphanumeric
# sets.

vowels = {'a','e','i','o','u'}

consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}


alpha = vowels.union(consonants)

alp_diff = alpha.difference(vowels)

Inter1 = consonants.intersection(vowels)

check_difference = alp_diff == consonants #to check if difference is equal or not


print(alp_diff)
print(len(alp_diff))
print(alpha)
print(len(alpha))
print(Inter1)
print("difference between output and consonants is: ",{check_difference})


numeric = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
alphanumeric = alpha.union(numeric)
Inter2 = vowels.intersection(alphanumeric)

print(alphanumeric)
print(len(alphanumeric))
print(Inter2)


