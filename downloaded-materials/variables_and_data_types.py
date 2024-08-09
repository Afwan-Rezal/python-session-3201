# Author: Nazrul Ismail
# Description: Template code for live demo of Python Basics (Var, data types and operators).
# Values are intentionally left None. Will be replaced during live coding.
# Date: 08/05/2024

# =============================================================================
# Section: Scalar Object Types
# -----------------------------------------------------------------------------
# Description:
# This section covers slide no. 14
# 
# Contents in this section:
# - Numeric (int, float)
# - bool 
# - None
# =============================================================================
# prints for Scalar Object Types
print("\n" + "="*30)
print("Section: Scalar Object Types")
print("="*30 + "\n")

# === Numeric ===
integer_var = 100
float_var = 3.141

# === Boolean ===
bool_var = True  # always uppercase on first letter

# === None type ===
none_var = None

print("Integer Variable:", integer_var, type(integer_var))
print("Float Variable:", float_var, type(float_var))
print("bool Variable:", bool_var, type(bool_var))
print("None Variable:", none_var, type(none_var))

# =============================================================================
# Section: Text Types
# -----------------------------------------------------------------------------
# Description:
# This section covers slide no. 15 and 16
# 
# Contents in this section:
# - Strings (str)
# - bool 
# - None
# =============================================================================

# Section: String
print("\n" + "="*30)
print("Section: Text type")
print("="*30 + "\n")

# Single or double quoated 
single_quote = None
double_quotes = None

name = "Moon"
greet = "hi" + name 
greeting = "hi" + " " + name

print("Single quote str Variable:", single_quote, type(single_quote))
print("Double quote str Variable:", double_quotes, type(double_quotes))
print("Boolean Variable:", bool_var, type(bool_var))

#print(greet)
#print(greeting)

silly = name * 3
print(silly)

#in-built functions for str 
print("Length of name: ", len(name))

#Slicing -> [start:stop:step]
#start: The index of the starting element (inclusive).
#stop: The index of the stopping element (exclusive).
#step: The interval between elements to include in the slice.
index = 0
print("Accessing a letter index in name:", name[index])

start_idx = 0
end_idx = 2
print("Accessing sliced at start and end idx in name:", name[start_idx:end_idx])

#operators with <, >, == on strs
name_2 = "Cat"
print(name < name_2)

#Reversing a string 
name_3 = "Tako"
name_3_reversed = name_3[::-1]
print("Reversed of name_3: ", name_3_reversed)

# === Typecasting ===
int_str = "123"
typecast_int = None
print("int_str:", int_str, type(int_str))
print("typecase_int:", typecast_int, type(typecast_int))

# =============================================================================
# Section: Sequence Types
# -----------------------------------------------------------------------------
# Description:
# This section covers slide no. 18-20
# 
# Contents in this section:
# - Lists
# - tuple 
# - dictionary (dict)
# =============================================================================

print("\n" + "="*30)
print("Section: Sequence")
print("="*30 + "\n")

# === List ===
list_var = [2, 'a', 4, [1, 2]]
print("List Variable:", list_var, type(list_var))

# Accessing a list element
index = 0
print(list_var[index])

# Slicing a list, e.g., from index 0 to 2
# caveat: does not include the last index i.e., 2
start_idx = 0
end_idx = 2
print(list_var[0:2])

# === Tuple ===
# Inherits the same properties as lists for accessing elements and slicing
# However, it is not immutable! i.e., elements cannot be changed
tuple_var = ()
print("Tuple Variable:", tuple_var, type(tuple_var))
#print(tuple_var[0], tuple_var[0:10])

# === Dictionary ===
# Represented as { key : value }
dictionary_var = {}
dictionary_var["key"] = None
print(dictionary_var)
print("Dictionary Variable:", dictionary_var, type(dictionary_var))