import sys


def main():
   filename = sys.argv[1]
   with open(filename) as f:
        content = f.readlines()
        numbers = list()
        total = 0
        for line in content:
            num = ""
            for letter in line:
                if letter.isdigit():
                    num +=letter
            
            numbers.append(int(""+ num[0] + num[-1]))
        print(numbers)
        total = sum(numbers)
        print(sum(numbers))





if __name__ == "__main__":
    main()
