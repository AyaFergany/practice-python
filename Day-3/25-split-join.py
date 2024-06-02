def split_join(line):
    new_line=line.split()
    final_line='-'.join(new_line)
    return final_line

if __name__ == '__main__':
    line=input()
    result=split_join(line)
    print(result)