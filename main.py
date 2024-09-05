def main():

    def count(file):

        words = file.split()
        count = len(words)

        return count
    
    def w_count(file):

        dic = {}

        alpha = "abcdefghijklmnopqrstuvwxyz"

        for i in alpha:
            dic[i] = None

        for i in alpha:
            count = 0
            for j in file:
                if i == j.lower():
                    count += 1
            dic[i] = count


        return dic

    def prnt(count, dic):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count} words found in the document\n")

        for i in dic:
            print(f"The '{i}' character was found {dic[i]} times")



    with open("/home/black_sheep/bootdev_tutorial/workspace/github.com/Blacksheep135/bookbot/books/frankenstein.txt") as f:

        file_contents = f.read()
        C = count(file_contents)
        dic = w_count(file_contents)
        prnt(C, dic)
    f.close()

    return 


main()

