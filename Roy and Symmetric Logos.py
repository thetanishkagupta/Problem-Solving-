# Check the symmetry row and column wise both

def verify_logo(logo , n):
    # y-axis
    for i in range(n):
        for j in range(n // 2):
            if logo[i][j] != logo[i][n - j - 1]:
                return False
    # x-axis 
    for i in range(n // 2):
        for j in range(n):
            if logo[i][j] != logo[n - i - 1][j]:
                return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    logo = []
    for r in range(n):
        row = input()
        logo.append(row)
    ans = verify_logo(logo , n)
    if ans:
        print("YES")
    else:
        print("NO")        
