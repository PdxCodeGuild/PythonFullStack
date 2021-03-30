



def peaks(data):
    # output = []
    # for i in range(1, len(data)-1):
    #     if data[i] > data[i-1] and data[i] > data[i+1]:
    #         output.append(i)
    # return output

    # output = []
    # for i in range(len(data)):
    #     if i == 0 or i == len(data)-1:
    #         continue
    #     if data[i] > data[i-1] and data[i] > data[i+1]:
    #         output.append(i)
    # return output


    # return [i for i in range(1, len(data)-1) if data[i] > data[i-1] and data[i] > data[i+1]]


    output = []
    for i in range(len(data)):
        # short-circuited evaluation
        if i != 0 and i != len(data)-1 and data[i] > data[i-1] and data[i] > data[i+1]:
            output.append(i)
    return output




def valleys(data):
    output = []
    for i in range(1, len(data)-1):
        if data[i-1] > data[i] < data[i+1]:
            output.append(i)
    return output


def peaks_and_valleys(data):
    return peaks(data) + valleys(data)



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(data)) # [6, 14]
print(valleys(data)) # [9, 17]
print(peaks_and_valleys(data)) # [6, 9, 14, 17]





