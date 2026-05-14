import json

def load_contacts():
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("contacts.json" , "w" , encoding="utf-8") as file:
        json.dump(contacts , file , ensure_ascii=False , indent=4 )

def add_contact():
    contacts = load_contacts()
    name = input("이름 입력:")
    duplicate = False
    for contact in contacts:
       if contact["name"] == name:
            duplicate = True 
            break
    if duplicate:
        print("이미 등록된 이름입니다.")
    else:
        while True:
            phone = input("전화번호 입력:")
            if phone.isdigit():
                break
            else:

                print("숫자만 입력하세요")
        email = input("이메일 입력:")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
            }

        contacts.append(contact)
        save_contacts(contacts)
        print("연락처가 추가 되었습니다")

def show_contacts():
    contacts = load_contacts()

    if not contacts:
        print("연락처가 없습니다")
    else: 
        for contact in contacts:
            print("이름:", contact ["name"], "전화번호:" , contact["phone"], "이메일:", contact["email"])
            
def search_contact():
    contacts = load_contacts()
    found = False
    search = input("검색어:")
    for contact in contacts:
        if search in contact["name"]:
            print("이름:", contact ["name"], "전화번호:" , contact["phone"], "이메일:", contact["email"])
            found = True
    if not found:
        print("검색된 연락처가 없습니다")

def update_contact():
    contacts = load_contacts()
    found = False
    name = input("이름 입력:")
    for contact in contacts:
        if name == contact["name"]:
            print("이름", contact["name"], "이메일", contact["email"])
            contact["phone"] = input("새 전화번호 입력:")
            contact["email"] = input("새 이메일 입력:")
            found = True
            break
    if found:
             save_contacts(contacts)
             print("저장되었습니다")

    else:
             print("찾을 수 없습니다")    
        
def delete_contact():
    contacts = load_contacts()
    deleted = False
    search = input("삭제할 이름:")
    for contact in contacts:
        if search == contact["name"]:
            contacts.remove(contact)
            deleted = True
            break
    if deleted:
        save_contacts(contacts)
        print("삭제되었습니다.")
    else:
        print("검색된 연락처가 없습니다.")
    
def main():
    while True:
        print("1.추가")
        print("2.전체보기")
        print("3.검색")
        print("4.수정")
        print("5.삭제")
        print("6.종료")

        choice = input("선택: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts() 
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()    
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("잘못된 선택입니다")

main()        






            


        
