# [0] EOF 예외처리
while True:
    try:
        # [1] 입력값 설정
        memory = [input() for _ in '_'*32]

        # [2] pc 순서대로 memory 읽어 실행하기
        result = 0
        pc = 0
        while True:
            byte = memory[pc]
            command = byte[0:3]
            x = int(byte[3:8], 2)
            pc = (pc+1) % 32

            # STA
            if command == '000':
                tmp = bin(result)[2:]
                while len(tmp) != 8:
                    tmp = '0'+tmp
                memory[x] = tmp
            # LDA
            elif command == '001':
                result = int(memory[x], 2)
            # BEQ
            elif command == '010':
                if result == 0:
                    pc = x
            # NOP
            elif command == '011':
                pass
            # DEC
            elif command == '100':
                result = (result-1)%256
            # INC
            elif command == '101':
                result = (result+1)%256
            # JMP
            elif command == '110':
                pc = x
            # HLT
            elif command == '111':
                tmp = bin(result)[2:]
                while len(tmp) != 8:
                    tmp = '0'+tmp
                print(tmp)
                break

    except EOFError:
        break