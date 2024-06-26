import random
import time
import sys

listOfValues = []


def main(values):
    maxItems = 20000
    maxNumber = 1000000
    minNumber = 1

    print(f"Setting Recursion Limit to {maxItems}")
    sys.setrecursionlimit(maxItems)

    print("Generating List")
    for i in range(maxItems):
        values.append(random.randint(minNumber, maxNumber))

    print("Testing Bubblesort")
    bubbleSortTest(values)

    print("Testing Insertion")
    insertionSortTest(values)

    print("Testing QuickSort Insertion")
    quickSortTestMain(values)

    print("Tests finished")


def bubbleSortTest(listToSort):
    startTime = time.time()

    length = len(listToSort)

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if listToSort[j] > listToSort[j + 1]:
                tempNum = listToSort[j + 1]
                listToSort[j + 1] = listToSort[j]
                listToSort[j] = tempNum

    endTime = time.time()

    finalTime = endTime - startTime

    print(f"Bubble Sort took a total of {str(finalTime)}ms ")
    print(listToSort)


def insertionSortTest(listToSort):
    startTime = time.time()

    length = len(listToSort)
    i = 1
    while i < length:
        z = listToSort[i]
        j = i
        while (j > 0) and (listToSort[j - 1] > z):
            listToSort[j] = listToSort[j - 1]
            j = j - 1
        listToSort[j] = z
        i = i + 1

    endTime = time.time()

    finalTime = endTime - startTime

    print(f"Insertion Sort took a total of {str(finalTime)}ms ")
    print(listToSort)


def quickSortTestMain(listToSort):
    startTime = time.time()

    # listToSort = quickSortTest(listToSort, 0, len(listToSort) - 1)
    listToSort = iterativeQuickSort(listToSort)

    endTime = time.time()
    finalTime = endTime - startTime

    print(f"Quick Sort took a total of {str(finalTime)}ms ")
    print(listToSort)


# Generated by ChatGPT
# This was necessary to avoid running into recursion limits
def iterativeQuickSort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = arr[start]
        low, high = start, end

        while low <= high:
            while low <= high and arr[low] < pivot:
                low += 1
            while low <= high and arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1

        stack.append((start, high))
        stack.append((low, end))

    return arr


def quickSortTest(L, anfang, ende):
    if L:
        pivot = L[anfang]
        links = anfang
        rechts = ende
        while links <= rechts:
            while L[links] < pivot:
                links = links + 1
            while L[rechts] > pivot:
                rechts = rechts - 1
            if links <= rechts:
                if links < rechts:
                    h = L[links]
                    L[links] = L[rechts]
                    L[rechts] = h
                links = links + 1
                rechts = rechts - 1
        if anfang < rechts:
            L = quickSortTest(L, anfang, rechts)
        if links < ende:
            L = quickSortTest(L, links, ende)
    return L


if __name__ == "__main__":
    main(listOfValues)
