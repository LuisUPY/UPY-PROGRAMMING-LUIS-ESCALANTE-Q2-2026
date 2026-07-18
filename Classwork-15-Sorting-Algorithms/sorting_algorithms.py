"""
Classwork 15 - Sorting Algorithms
Step-by-step visualization of bubble, insertion, and selection sort using stddraw.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stddraw


def draw_bars(arr, highlight=None, finalized=None, delay=300):
    """
    Draw a bar chart for the current array state.
    highlight: indices to mark in red (active comparison or swap)
    finalized: indices already in their final sorted position (green)
    """
    n = len(arr)
    if n == 0:
        return

    stddraw.clear()
    max_val = max(arr)
    if max_val == 0:
        max_val = 1

    bar_width = 1.0 / n
    highlight = highlight or []
    finalized = finalized or []

    for i in range(n):
        x = i * bar_width
        height = (arr[i] / max_val) * 0.95

        if i in highlight:
            stddraw.setPenColor(stddraw.RED)
        elif i in finalized:
            stddraw.setPenColor(stddraw.DARK_GREEN)
        else:
            stddraw.setPenColor(stddraw.BOOK_BLUE)

        stddraw.filledRectangle(x, 0, bar_width * 0.9, height)

    stddraw.show(delay)


def bubble_sort(arr):
    """Sort arr in place using bubble sort with early-stop optimization."""
    n = len(arr)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort_animated(arr):
    """Animate bubble sort by redrawing bars after each comparison or swap."""
    n = len(arr)
    stddraw.setCanvasSize(800, 400)
    stddraw.setXscale(0, 1)
    stddraw.setYscale(0, 1)

    for pass_num in range(n - 1):
        swapped = False
        finalized = list(range(n - pass_num, n))

        for i in range(n - 1 - pass_num):
            draw_bars(arr, highlight=[i, i + 1], finalized=finalized)
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                draw_bars(arr, highlight=[i, i + 1], finalized=finalized)

        if not swapped:
            break

    draw_bars(arr, finalized=list(range(n)), delay=1000)
    return arr


def insertion_sort(arr):
    """Sort arr in place using insertion sort."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def insertion_sort_animated(arr):
    """Animate insertion sort by showing each shift and insertion."""
    n = len(arr)
    stddraw.setCanvasSize(800, 400)
    stddraw.setXscale(0, 1)
    stddraw.setYscale(0, 1)

    draw_bars(arr, finalized=[0])

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        draw_bars(arr, highlight=[i], finalized=list(range(i)))

        while j >= 0 and arr[j] > key:
            draw_bars(arr, highlight=[j, j + 1], finalized=list(range(i)))
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        draw_bars(arr, highlight=[j + 1], finalized=list(range(i + 1)))

    draw_bars(arr, finalized=list(range(n)), delay=1000)
    return arr


def selection_sort(arr):
    """Sort arr in place using selection sort."""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def selection_sort_animated(arr):
    """Animate selection sort by highlighting the current minimum search."""
    n = len(arr)
    stddraw.setCanvasSize(800, 400)
    stddraw.setXscale(0, 1)
    stddraw.setYscale(0, 1)

    for i in range(n - 1):
        min_idx = i
        finalized = list(range(i))

        for j in range(i + 1, n):
            draw_bars(arr, highlight=[j, min_idx], finalized=finalized)
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            draw_bars(arr, highlight=[i, min_idx], finalized=finalized)

    draw_bars(arr, finalized=list(range(n)), delay=1000)
    return arr


def parse_numbers(text):
    """Convert a space-separated string into a list of integers."""
    parts = text.strip().split()
    if not parts:
        raise ValueError("No numbers were entered.")
    return [int(part) for part in parts]


def main():
    # INPUT
    raw_input = input("Enter numbers separated by spaces: ")
    algorithm = input("Choose algorithm (bubble / insertion / selection): ").strip().lower()
    animate = input("Show animation? (yes / no): ").strip().lower()

    original = parse_numbers(raw_input)
    working = original.copy()

    # PROCESS
    if animate == "yes":
        if algorithm == "bubble":
            bubble_sort_animated(working)
        elif algorithm == "insertion":
            insertion_sort_animated(working)
        elif algorithm == "selection":
            selection_sort_animated(working)
        else:
            print("Invalid algorithm. Use bubble, insertion, or selection.")
            return
    else:
        if algorithm == "bubble":
            bubble_sort(working)
        elif algorithm == "insertion":
            insertion_sort(working)
        elif algorithm == "selection":
            selection_sort(working)
        else:
            print("Invalid algorithm. Use bubble, insertion, or selection.")
            return

    # OUTPUT
    print("Original array:", original)
    print("Sorted array:  ", working)


if __name__ == "__main__":
    main()
