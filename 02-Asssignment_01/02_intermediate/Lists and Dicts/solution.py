import random
def accessing_elem(list, index):
    print(list)
    print(f"Index {index} contains '{list[index]}' ")

def modifying_elem(list, index, new_val):
    print(list)
    list[index] = new_val
    print(list)
    
def slicing_list(list, start_idx, end_idx):
    print(list)
    new_list = slice(start_idx, end_idx)
    print(list[new_list])    

def main():
    choice = input("Select an operation (access, modify, slice): ").lower()
    
    # Accession
    if choice == 'access':
        user_items = input("Create the list. Enter some words separated by commas (,): ")
        user_list = user_items.split(',')
        user_index = int(input("Enter the index to see the item: "))
        if user_index > len(user_list):
            print("No indexes available for your list") 
        else: 
            print("Loading...")
        accessing_elem(user_list, user_index) 
    
    
    # Modification
    elif choice == 'modify':
        user_items = input("Create the list. Enter some words separated by commas (,): ")
        user_list = user_items.split(',')
        user_index = int(input("Enter the index to change the item: "))
        
        while user_index != len(user_list) - 1:
            print(f"No indexes available. There are only {len(user_list)} items") 
            user_index = int(input("Enter the index to change the item: "))
        else: 
            print("Loading...")
                
        new_val = input("Enter the new item to modify: ")
        modifying_elem(user_list, user_index, new_val)
        
        
    # Slicing
    elif choice == 'slice':
        user_items = input("Create the list. Enter some words separated by commas (,): ")
        user_list = user_items.split(',')
        start_index = int(input("Enter the starting index to slice: "))
        
        while start_index < 0 or start_index >= len(user_list):
            print(f"No indexes available. There are only {len(user_list)} items") 
            user_index = int(input("Enter the starting index to slice: "))
        else: 
            print("Loading...")
            
        end_index = int(input("Enter the ending index to stop: "))
        
        while end_index < 0 or end_index > len(user_list):
            print(f"No indexes available. There are only {len(user_list)} items") 
            user_index = int(input("Enter the ending index to slice: "))
        else: 
            print("Loading...")
            
        slicing_list(user_list, start_index, end_index)
        
    
    # friends = ['ahmed', 'yousuf', 'abdullah', 'sabih']
    # index = random.randint(0, len(friends))
    # new_friend = random.choices(['abubakar', 'saad', 'shuraim'])
     
    # accessing_elem(friends, index)
    # modifying_elem(friends, index, new_friend)
    # slicing_list(friends, 2, 3)
    
if __name__ == '__main__':
    main()