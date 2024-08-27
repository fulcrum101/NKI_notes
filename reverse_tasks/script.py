def main():
    with open('flag.bluehens', 'rb') as f:
        data = f.read()

    data = data.decode('utf-8')
    lines = data.split('\n')
    words = []
    for line in lines:
        words.append(line.split(' '))
    res = ''
    I = 0
    REGISTER = 0
    COUNTER = 0
    while I < len(words):
        line = words[I]
        op = line.count('blue')
        arg = line.count('hens')
        match op:
            case 1:
                REGISTER = arg
                I += 1
            case 2:
                REGISTER += arg
                I += 1
            case 3:
                REGISTER -= arg
                I += 1
            case 4:
                REGISTER *= arg
                I += 1
            case 5:
                I = arg-1
            case 6:
                I -= arg
            case 7:
                I += arg
            case 8:
                COUNTER += arg
                I +=1
            case 9:
                COUNTER -= arg
                I+=1
            case 10:
                if COUNTER == 0:
                    I += 2
                else:
                    I+=1
            case 11: 
                res += chr(REGISTER)
                I += 1
            case _:
                pass

    with open('code.txt', 'w+') as res_file:
        res_file.write(res)
    

if __name__ == '__main__':
    main()