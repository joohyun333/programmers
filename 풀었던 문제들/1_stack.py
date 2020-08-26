def serch_CAMBRIDGE(write):
    w = list(str(write))
    ban_list = list('CAMBRIDGE')
    for i in range(len(w)):
        for j in range(len(ban_list)):
            while w[i] == ban_list[j]:
                w.remove(w[i])
                print(w)
    return "".join(w)

if __name__ == "__main__":
    a= str(input())
    print(serch_CAMBRIDGE(a))