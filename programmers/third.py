def solution(clothes):
    clothesTypeMap = {}

    for clothe, clothesType in clothes:
        print(clothe)
        print("clothesType : ", clothesType)

        clothesTypeMap[clothesType] = clothesTypeMap.get(clothesType, 0) + 1

        print(clothesTypeMap)

    answer = 1
    for clothesType in clothesTypeMap:
        answer *= (clothesTypeMap[clothesType] + 1)

    return answer - 1