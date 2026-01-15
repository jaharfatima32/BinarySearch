# BinarySearch
🔍 Binary Search (Easy Explanation)

Binary Search is a fast searching technique, but it works only on sorted lists.
It repeatedly divides the list into two halves to find the required element.

🧠 How Binary Search Works

Make sure the list is sorted.

Set
low = 0
high = len(list) - 1

Find the middle element:
mid = (low + high) // 2

Compare the middle element with the target:

If equal → item found

If target is greater → search right half

If target is smaller → search left half

Repeat until found or low > high.

If not found → item not present.

🧪 Example

List: [2, 5, 8, 12, 16, 23, 38]
Target: 16

Middle = 12 → target is greater → right side

Middle = 23 → target is smaller → left side

Middle = 16 → Found

✅ Advantages

Very fast

Efficient for large datasets

❌ Disadvantages

List must be sorted

Slightly harder than linear search

🔁 Linear Search vs Binary Search
Feature	Linear Search	Binary Search
Sorted list needed	❌ No	✅ Yes
Speed	Slow	Fast
Complexity	O(n)	O(log n)

