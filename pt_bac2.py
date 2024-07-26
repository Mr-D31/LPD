import math

def giaiPTBac2(a, b, c):
    '''
    Tính nghiệm của phương trình bậc 2 có dạng ax^2 + bx + c = 0

    Args:
    a, b, c (float): lần lượt là các hệ số của phương trình bậc 2
    Return:
    float: nghiệm của phương trình
    '''
    
    # Kiểm tra các hệ số
    if a == 0:
        if b == 0:
            print("Phương trình vô nghiệm!")
        else:
            print(f"Phương trình có một nghiệm: x = {-c / b}")
        return

    # Tính delta
    delta = b * b - 4 * a * c

    # Tính nghiệm
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có 2 nghiệm là: x1 = {x1} và x2 = {x2}")
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f"Phương trình có nghiệm kép: x1 = x2 = {x1}")
    else:
        print("Phương trình vô nghiệm!")

# Nhập các hệ số
a = float(input("Nhập hệ số bậc 2, a = "))
b = float(input("Nhập hệ số bậc 1, b = "))
c = float(input("Nhập hằng số tự do, c = "))

# Gọi hàm giải phương trình bậc 2
giaiPTBac2(a, b, c)
