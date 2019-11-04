def main():
    x, y = 10, 100
  
    # conditional flow uses if, elif, else  
    if (x < y):
        msg = "x is less than y"
    elif (x == y):
        msg = "x is same as y"
    else:
        msg = "x is greater than y"
    print(msg)

    # conditional statements let you use "a if C else b"
    msg = "x is less than y" if (x < y) else " x is greater than or equal to y"
    print(msg)

if __name__ == "__main__":
    main()