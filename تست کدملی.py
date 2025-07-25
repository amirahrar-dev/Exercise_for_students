
def test_national_code(code):
    code=str(code)
    if not(code.isnumeric()) or len(code)!=10 or code in ("0000000000","1111111111","2222222222","3333333333","4444444444","5555555555","6666666666","7777777777","8888888888","9999999999"):
        return False
    else:
        Sum=0
        for i in range (0,9):
            Sum+=int(code[i])*(10-i)
        if Sum%11<2 and int(Sum%11)==int(code[9]):
            return True
        elif int(11-(Sum%11))==int(code[9]):
            return True
        else :return False

