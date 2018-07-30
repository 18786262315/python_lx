def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        print(bar("2"))
    except Exception as e:
        print("Error:", e)

    finally:
        print("finally...")
main()