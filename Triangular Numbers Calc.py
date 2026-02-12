while True:
    print("What do you wanna calc is it just one number (1) or is it every number up to that number (2) [q to quit]")
    ans = input("> ").strip().lower()
    if ans == "1" :
        while True:
            ext = input("Enter a number : ").strip()
            try :
                ext = int(ext)
            except:
                print("Enter a number!!")
            print(f"{ext} : {(ext*(ext+1))/2}")
            break
    elif ans == "2" :
        while True:
            ext = input("Enter a number : ").strip()
            try :
                ext = int(ext)
            except:
                print("Enter a number!!")
            for num in range(1,ext+1):
                print(f"{num} : {(num*(num+1))/2}")
            break
    elif ans == "q" :
        quit()
    else :
        print("Try again !")