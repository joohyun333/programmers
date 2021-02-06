import string
def solution(new_id):
    m = string.punctuation.replace("-","").replace("_","").replace(".","")
    new_id = new_id.lower() #1
    for i in m:
        new_id = new_id.replace(i,"")  #2
    while ".." in new_id:
        new_id = new_id.replace("..",".") #3
    new_id = new_id.strip(".").lstrip(".") #4
    if new_id == "" : new_id = "a" #5
    new_id = new_id[:15].strip(".") #6
    if len(new_id)<=2:
        while len(new_id)<3:
            new_id = new_id+new_id[-1]#7
    return new_id
if __name__ == "__main__":
    strs = 	"=.="
    print(solution(strs))