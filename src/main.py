from auth import register, login
from journal import add_entry, view_entries
from screening import score_phq9, save_screening

def main():
    print("Welcome. Type 1 to register, 2 to login:")
    choice = input("> ").strip()
    if choice == '1':
        u = input("Username: ")
        p = input("Password: ")
        register(u,p)
        print("Registered.")
        return
    elif choice == '2':
        u = input("Username: ")
        p = input("Password: ")
        user = login(u,p)
        if not user: 
            print("Login failed") 
            return
        print(f"Welcome {u}!")
        while True:
            cmd = input("Command (add/view/screen/exit): ").strip()
            if cmd == 'add':
                t = input("Title: ")
                b = input("Body: ")
                m = int(input("Mood (0-10): "))
                add_entry(user['id'],t,b,m)
                print("Saved.")
            elif cmd == 'view':
                for e in view_entries(user['id']):
                    print(e)
            elif cmd == 'screen':
                ans = [int(input(f"Q{i} (0-3): ")) for i in range(1,10)]
                s, cat = score_phq9(ans)
                save_screening(user['id'], 'PHQ-9', s, ans)
                print(f"Score {s} ({cat})")
            elif cmd == 'exit':
                break
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
