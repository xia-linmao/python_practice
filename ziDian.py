if __name__ == '__main__':
    content = "maozi maozi mia mia mia mia zi mia zi mao mao jiao"
    content1 = content.split(" ")
    result = {}

    for j in content1:
        if j in result:
            result[j] = result[j] +1
        else:
            result[j] = 1
    print(result)



    # {"maozi": 5, "miazi": 4....}
