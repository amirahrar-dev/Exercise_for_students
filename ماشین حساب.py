while True:
  a=int(input("عدد اول را وارد کنید :"))
  print("عملیات های قابل قبول : + , - , * , / , exit")
  op=input("عملیات خودرا وارد کنید :")
  if op=="exit":break
  b=int(input("عدد دوم را وارد کنید :"))
  if op=="+":
    print(a+b)
  elif op=="-":
    print(a-b)
  elif op=="*":
    print(a*b)
  elif op=="/":
    print(a/b)
  else:
    print("عملیات مورد نظر یافت نشد لطفا دوباره وارد کنید")
