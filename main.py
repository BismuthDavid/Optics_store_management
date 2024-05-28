class Prescription:
    def __init__(self, r_eye, l_eye):
        self.r_eye = r_eye
        self.l_eye = l_eye

    def __str__(self):
        return f"right eye: {self.r_eye}, left eye: {self.l_eye}"


class Order:
    def __init__(self, frame_type, glass_type, glass_idx, frame_price, glass_price, buy_date):
        self.frame_type = frame_type
        self.glass_type = glass_type
        self.glass_idx = glass_idx
        self.frame_price = frame_price
        self.glass_price = glass_price
        self.buy_date = buy_date
        self.total_price = frame_price + glass_price

    def __str__(self):
        print(f"frame type: {self.frame_type}, glass type: : {self.glass_type}, glass index: : {self.glass_idx}, "
              f"frame price: {self.frame_price}, glass price: {self.glass_price}, buy date: {self.buy_date}, "
              f"total price: {self.total_price}")

class Client:
    def __init__(self, name, id, phone):
        self.name = name
        self.id = id
        self.phone = phone
        self.prescription_list = []
        self.order_list = []


list_of_clients = []


def add_a_client():
    name = input("אנא הכנס את שמו של הלקוח:\n")
    id = input("אנא הכנס את תעודת הזהות של הלקוח:\n")
    phone = input("אנא הכנס את הטלפון הנייד של הלקוח:\n")
    new_obj = Client(name, id, phone)
    return new_obj

def add_a_prescription():
    r_eye_sphere = input("מספר עין ימין\n")
    r_eye_cylinder = input("צילינדר עין ימין\n")
    r_eye_axis = input("Axis עין ימין\n")
    r_eye_pd = input("PD עין ימין\n")
    r_eye_pupil = input("גובה אישון ימין\n")
    l_eye_sphere = input("מספר עין שמאל\n")
    l_eye_cylinder = input("צילינדר עין שמאל\n")
    l_eye_axis = input("Axis עין שמאל\n")
    l_eye_pd = input("PD עין שמאל\n")
    l_eye_pupil = input("גובה אישון שמאל\n")
    right_eye = f"""sphere: {r_eye_sphere}, cylinder: {r_eye_cylinder}, axis: {r_eye_axis}, 
    pd: {r_eye_pd}, pupil: {r_eye_pupil}"""
    left_eye = f"""sphere: {l_eye_sphere}, cylinder: {l_eye_cylinder}, axis: {l_eye_axis}, 
    pd: {l_eye_pd}, pupil: {l_eye_pupil}"""
    new_prescription = Prescription(right_eye, left_eye)
    return new_prescription


def add_new_order():
    frame_type = input("הכנס דגם מסגרת\n")
    glass_type = input("הכנס שם עדשה\n")
    glass_idx = input("הכנס אינדקס עדשה\n")
    frame_price = int(input("הכנס עלות מסגרת\n"))
    glass_price = int(input("הכנס עלות עדשות\n"))
    buy_date = input("הכנס תאריך רכישה\n")
    new_order = Order(frame_type, glass_type, glass_idx, frame_price, glass_price, buy_date)
    return new_order


while True:
    request = int(input("""
        מה ברצונך לבצע היום?
        להוספת לקוח אנא הקש 0
        לעדכון סלולרי של לקוח אנא הקש 1
        להוספת מרשם ללקוח אנא הקש 2
        להוספת עסקה חדשה אנא הקש 3 
        להדפסת הלקוחות הקיימים הקש 4
        להדפסת פרטי לקוח קיים הקש 5
        """))
    if request == 0:
        print("-----------------------------------------------------------------")
        new_client = add_a_client()
        list_of_clients.append(new_client)
        print("-----------------------------------------------------------------")

    elif request == 1:
        print("-----------------------------------------------------------------")
        isnt_a_client = True
        id = input("אנא הכנס את תעודת הזהות של לקוח קיים:\n")
        print("-----------------------------------------------------------------")
        for client in list_of_clients:
            if client.id == id:
                phone = input("הכנס טלפון נייד חדש ללקוח\n")
                print("-----------------------------------------------------------------")
                client.phone = phone
                print("הטלפון עודכן בהצלחה")
                print("-----------------------------------------------------------------")
                isnt_a_client = False
        if isnt_a_client:
            print("הלקוח לא קיים, אנא הקם כרטיס לקוח חדש עבורו")
            print("-----------------------------------------------------------------")

    elif request == 2:
        print("-----------------------------------------------------------------")
        isnt_a_client = True
        id = input("אנא הכנס את תעודת הזהות של לקוח קיים:\n")
        print("-----------------------------------------------------------------")
        for client in list_of_clients:
            if client.id == id:
                client.prescription_list.append(add_a_prescription())
                isnt_a_client = False
        if isnt_a_client:
            print("הלקוח לא קיים, אנא הקם כרטיס לקוח חדש עבורו")
        print("-----------------------------------------------------------------")

    elif request == 3:
        print("-----------------------------------------------------------------")
        isnt_a_client = True
        id = input("אנא הכנס את תעודת הזהות של לקוח קיים:\n")
        print("-----------------------------------------------------------------")
        for client in list_of_clients:
            if client.id == id:
                client.order_list.append(add_new_order())
                isnt_a_client = False
        if isnt_a_client:
            print("הלקוח לא קיים, אנא הקם כרטיס לקוח חדש עבורו")
        print("-----------------------------------------------------------------")

    elif request == 4:
        print("-----------------------------------------------------------------")
        for client in list_of_clients:
            print(f"name: {client.name}, id: {client.id}, phone: {client.phone}")
            print("-----------------------------------------------------------------")

    elif request == 5:
        print("-----------------------------------------------------------------")
        isnt_a_client = True
        id = input("אנא הכנס את תעודת הזהות של לקוח קיים:\n")
        print("-----------------------------------------------------------------")
        for client in list_of_clients:
            if client.id == id:
                print(f"name: {client.name}, id: {client.id}, phone: {client.phone}")
                for prescription in client.prescription_list:
                    print(f"prescription: {prescription}")
                for order in client.order_list:
                    print(order)
                print("-----------------------------------------------------------------")

