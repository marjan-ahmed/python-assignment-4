import time 

def main():
    user_time = int(input("Enter the time to pause: ")) 
    while user_time > 0:
        print(f"Time left: {user_time} sec")
        time.sleep(1)  
        user_time -= 1 
    print("Time's up!")
    
    
if __name__ == '__main__':
    main()