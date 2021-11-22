# Creating the list in which the number will be searched
ls = [1,3,2,4,5,6,9,8,7,10]

# Sorting the list in order to make effective the later search
ls.sort()

# Creating first, last and mid indexes
first = 0
last = len(ls) - 1
mid = (first+last) // 2

# Asks the user to input a number to be searched on the previous list
item = int(input("Enter the number to be searched: "))

# Logic condition that shows if the number was found or not
found = False

# Loop that is used to search the number on the list
# While we still have items to search and we haven't found the number yet...
while (first <= last and not found):
    # Update the mid index
    mid = (first + last) // 2
    # If mid index is the number we're searching for
    if ls[mid] == item:
        # Print the location for the number
        print(f"Found at location {mid}")
        # Set the logic condition to True
        found = True
    # If mid index is not the number we're searching for
    else:
        # If the number we're searching for is lower than the mid index
        if item < ls[mid]:
            # The last index now becomes the mid index - 1, so we end up with the left part of the current list
            last = mid - 1
        # If the number we're searching for is higher than the mid index
        else:
            # The first index now becomes the mid index + 1, so we end up with the right part of the current list
            first = mid + 1
# If, after the loop, we haven't found the number
if found == False:
    # Print that the number wasn't found
    print("Number not found")