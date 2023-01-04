from copy import deepcopy
def solution(sourceArray, destinationArray):
    uncorruptedTempArray, uncorruptedArray = [], []
    result = []
    if (len(sourceArray) == len(sourceArray)) and len(sourceArray) == 1:
        if sourceArray[0] == destinationArray[0]:
            return [1, 0]
        else:
            return [0, 0]


    for i in range(len(sourceArray)):
        if sourceArray[i] == destinationArray[i]:
            if len(uncorruptedTempArray) == 0:
                uncorruptedTempArray.append(i)
            uncorruptedTempArray.append(sourceArray[i])

        else:
            if len(uncorruptedTempArray) > len(uncorruptedArray):
                uncorruptedArray = uncorruptedTempArray
                uncorruptedTempArray = []
            if (len(uncorruptedTempArray) == len(uncorruptedArray)) and len(uncorruptedArray)==0 :
                return [0,0]

    if len(uncorruptedArray) > 0 or len(uncorruptedTempArray) > 0:
        if len(uncorruptedArray) >= len(uncorruptedTempArray):

            if len(uncorruptedArray) == 0:
                return [0, 0]
            else:
                result.append(len(uncorruptedArray) - 1)
                result.append(uncorruptedArray[0])
        else:
            if len(uncorruptedTempArray) == 0:
                return [0, 0]
            else:
                result.append(len(uncorruptedTempArray) - 1)
                result.append(uncorruptedTempArray[0])

    return result

sourceArray = [33531593, 96933415, 28506400, 39457872, 29684716, 86010806]
destinationArray = [33531593, 96913415, 28506400, 39457872, 29684716, 86010806]
print(solution(sourceArray, destinationArray))