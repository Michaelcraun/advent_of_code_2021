def load():
    with open('day1.txt') as file:
        return file.readlines()

def measureSingleDepths():
    depths = load()
    currentDepth = 0
    increaseCount = 0
    for depth in depths:
        number = int(depth)
        state = ''
        if currentDepth == 0: state = 'N/A - no previous measurement'
        elif currentDepth < number: state = 'increased'
        elif currentDepth > number: state = 'decreased'

        if state == 'increased': increaseCount += 1
        print('{} ({})'.format(number, state))

        currentDepth = number
    print('The depth increased {} times'.format(increaseCount))

def measuerDepthsWithSlidingWindows():
    depths = load()
    
    sums = []
    for index in range(len(depths)):
        if index + 2 < len(depths):
            sum = int(depths[index]) + int(depths[index + 1]) + int(depths[index + 2])
            sums.append(sum)
            
    # Compare each summed depth
    currentSum = 0
    increaseCount = 0
    for sum in sums:
        state = ''
        if currentSum == 0: state = 'N/A - no previous sum)'
        elif currentSum < sum: state = 'increased'
        elif currentSum > sum: state = 'decreased'
        elif currentSum == sum: state = 'no change'

        if state == 'increased': increaseCount += 1
        print('{} ({})'.format(sum, state))

        currentSum = sum
    print('The depth increased {} times'.format(increaseCount))

    # def measuerDepthsWithSlidingWindows():
    # depths = load()
    
    # # Group depths and sum them
    # currentGroup = []
    # groupSize = 3
    # depthSums = []
    # for depth in depths:
    #     number = int(depth)
    #     currentGroup.append(number)
    #     if len(currentGroup) == groupSize:
    #         currentGroupDepth = 0
    #         for num in currentGroup: currentGroupDepth += num
    #         depthSums.append(currentGroupDepth)
    #         currentGroup = []
        
    # # Compare each summed depth
    # currentSum = 0
    # increaseCount = 0
    # for sum in depthSums:
    #     state = ''
    #     if currentSum == 0: state = 'N/A - no previous sum)'
    #     elif currentSum < sum: state = 'increased'
    #     elif currentSum > sum: state = 'decreased'
    #     elif currentSum == sum: state = 'no change'

    #     if state == 'increased': increaseCount += 1
    #     print('{} ({})'.format(sum, state))

    #     currentSum = sum
    # print('The depth increased {} times'.format(increaseCount))

# measureSingleDepths()
measuerDepthsWithSlidingWindows()