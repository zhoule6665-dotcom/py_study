while True:
    try :
        x  = int(input("输入math"))
        
    except:
        print(f"{x}不是math是{type(x)}")
    else:
        print(f"math是{x}")
    finally:
        key  = input("是否继续 y or n")
        if key =="y" or key == "Y":
            continue
        else:
            exit(0)
