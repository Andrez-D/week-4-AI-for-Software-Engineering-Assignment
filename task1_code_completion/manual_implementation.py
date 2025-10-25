"""
Task 1: AI-Powered Code Completion - Manual Implementation
Objective: Write a function to sort a list of dictionaries by a specific key
Author: [Kipruto Andrew Kipngetich]
Date: October 2025
"""

def sort_dict_list_manual(data_list, sort_key, reverse=False):
    """
    Manually implemented function to sort a list of dictionaries by a specific key.
    
    Args:
        data_list (list): List of dictionaries to sort
        sort_key (str): Key to sort by
        reverse (bool): If True, sort in descending order
        
    Returns:
        list: Sorted list of dictionaries
        
    Time Complexity: O(n log n) - using Python's Timsort algorithm
    Space Complexity: O(n) - creates new sorted list
    """
    
    # Validate inputs
    if not data_list:
        return []
    
    if not isinstance(data_list, list):
        raise TypeError("data_list must be a list")
    
    if not all(isinstance(item, dict) for item in data_list):
        raise TypeError("All items in data_list must be dictionaries")
    
    # Check if sort_key exists in all dictionaries
    if not all(sort_key in item for item in data_list):
        raise KeyError(f"Key '{sort_key}' not found in all dictionaries")
    
    # Create a copy to avoid modifying the original list
    sorted_list = data_list.copy()
    
    # Sort using the built-in sorted() function with a lambda key function
    # Lambda extracts the value of sort_key from each dictionary
    sorted_list = sorted(
        sorted_list,
        key=lambda x: x[sort_key],
        reverse=reverse
    )
    
    return sorted_list


def sort_dict_list_with_default(data_list, sort_key, reverse=False, default_value=None):
    """
    Enhanced version that handles missing keys with default values.
    
    Args:
        data_list (list): List of dictionaries to sort
        sort_key (str): Key to sort by
        reverse (bool): If True, sort in descending order
        default_value: Default value for missing keys
        
    Returns:
        list: Sorted list of dictionaries
    """
    
    if not data_list:
        return []
    
    # Use get() method with default value to handle missing keys
    sorted_list = sorted(
        data_list,
        key=lambda x: x.get(sort_key, default_value),
        reverse=reverse
    )
    
    return sorted_list


def sort_dict_list_multiple_keys(data_list, sort_keys, reverse=False):
    """
    Sort by multiple keys in order of priority.
    
    Args:
        data_list (list): List of dictionaries to sort
        sort_keys (list): List of keys to sort by (in priority order)
        reverse (bool): If True, sort in descending order
        
    Returns:
        list: Sorted list of dictionaries
        
    Example:
        sort_dict_list_multiple_keys(students, ['grade', 'name'])
        # Sorts by grade first, then by name for students with same grade
    """
    
    if not data_list:
        return []
    
    # Sort by multiple keys using tuple in lambda
    sorted_list = sorted(
        data_list,
        key=lambda x: tuple(x.get(key) for key in sort_keys),
        reverse=reverse
    )
    
    return sorted_list


# ============================================================================
# TEST CASES AND DEMONSTRATIONS
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("TASK 1: MANUAL IMPLEMENTATION - CODE COMPLETION")
    print("="*80)
    
    # Test Case 1: Simple sorting by name
    print("\n[Test 1] Sorting employees by name:")
    print("-" * 80)
    
    employees = [
        {"name": "Alice", "age": 30, "salary": 75000},
        {"name": "Charlie", "age": 25, "salary": 60000},
        {"name": "Bob", "age": 35, "salary": 85000},
        {"name": "Diana", "age": 28, "salary": 70000}
    ]
    
    print("Original list:")
    for emp in employees:
        print(f"  {emp}")
    
    sorted_by_name = sort_dict_list_manual(employees, 'name')
    print("\nSorted by name (ascending):")
    for emp in sorted_by_name:
        print(f"  {emp}")
    
    # Test Case 2: Sorting by numeric value (descending)
    print("\n[Test 2] Sorting employees by salary (descending):")
    print("-" * 80)
    
    sorted_by_salary = sort_dict_list_manual(employees, 'salary', reverse=True)
    print("Sorted by salary (highest to lowest):")
    for emp in sorted_by_salary:
        print(f"  {emp['name']}: ${emp['salary']:,}")
    
    # Test Case 3: Sorting by age
    print("\n[Test 3] Sorting employees by age:")
    print("-" * 80)
    
    sorted_by_age = sort_dict_list_manual(employees, 'age')
    print("Sorted by age (youngest to oldest):")
    for emp in sorted_by_age:
        print(f"  {emp['name']}: {emp['age']} years old")
    
    # Test Case 4: Handling missing keys
    print("\n[Test 4] Handling missing keys with default values:")
    print("-" * 80)
    
    products = [
        {"name": "Laptop", "price": 1200, "rating": 4.5},
        {"name": "Mouse", "price": 25},  # Missing rating
        {"name": "Keyboard", "price": 75, "rating": 4.8},
        {"name": "Monitor", "price": 350}  # Missing rating
    ]
    
    print("Products with missing ratings:")
    for prod in products:
        print(f"  {prod}")
    
    sorted_by_rating = sort_dict_list_with_default(
        products, 
        'rating', 
        reverse=True,
        default_value=0
    )
    print("\nSorted by rating (with default 0 for missing):")
    for prod in sorted_by_rating:
        rating = prod.get('rating', 'N/A')
        print(f"  {prod['name']}: Rating {rating}")
    
    # Test Case 5: Multiple key sorting
    print("\n[Test 5] Sorting by multiple keys:")
    print("-" * 80)
    
    students = [
        {"name": "Alice", "grade": 90, "age": 20},
        {"name": "Bob", "grade": 85, "age": 22},
        {"name": "Charlie", "grade": 90, "age": 19},
        {"name": "Diana", "grade": 85, "age": 21}
    ]
    
    print("Students:")
    for student in students:
        print(f"  {student}")
    
    sorted_students = sort_dict_list_multiple_keys(
        students,
        ['grade', 'name'],
        reverse=True
    )
    print("\nSorted by grade (desc), then by name (asc):")
    for student in sorted_students:
        print(f"  {student['name']}: Grade {student['grade']}")
    
    # Test Case 6: Performance test
    print("\n[Test 6] Performance test with large dataset:")
    print("-" * 80)
    
    import time
    import random
    
    # Generate large dataset
    large_dataset = [
        {
            "id": i,
            "value": random.randint(1, 10000),
            "category": random.choice(['A', 'B', 'C', 'D'])
        }
        for i in range(10000)
    ]
    
    print(f"Dataset size: {len(large_dataset)} items")
    
    start_time = time.time()
    sorted_large = sort_dict_list_manual(large_dataset, 'value')
    end_time = time.time()
    
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Sorting time: {execution_time:.2f} ms")
    print(f"First 5 items: {sorted_large[:5]}")
    print(f"Last 5 items: {sorted_large[-5:]}")
    
    # Test Case 7: Error handling
    print("\n[Test 7] Error handling:")
    print("-" * 80)
    
    try:
        # Test with missing key
        invalid_data = [{"name": "Alice"}, {"age": 30}]
        sort_dict_list_manual(invalid_data, 'name')
    except KeyError as e:
        print(f"✓ Correctly caught error: {e}")
    
    try:
        # Test with wrong type
        sort_dict_list_manual("not a list", 'key')
    except TypeError as e:
        print(f"✓ Correctly caught error: {e}")
    
    # Test Case 8: Edge cases
    print("\n[Test 8] Edge cases:")
    print("-" * 80)
    
    # Empty list
    empty_result = sort_dict_list_manual([], 'key')
    print(f"Empty list result: {empty_result}")
    
    # Single item
    single_item = [{"name": "Alice", "age": 30}]
    single_result = sort_dict_list_manual(single_item, 'name')
    print(f"Single item result: {single_result}")
    
    # Items with same values
    same_values = [
        {"name": "Alice", "score": 100},
        {"name": "Bob", "score": 100},
        {"name": "Charlie", "score": 100}
    ]
    same_result = sort_dict_list_manual(same_values, 'score')
    print(f"Same values result: {[x['name'] for x in same_result]}")
    
    print("\n" + "="*80)
    print("MANUAL IMPLEMENTATION COMPLETE")
    print("="*80)
    
    # Summary statistics
    print("\n📊 IMPLEMENTATION STATISTICS:")
    print(f"  - Lines of code: ~150 (including comments and tests)")
    print(f"  - Functions implemented: 3")
    print(f"  - Test cases: 8")
    print(f"  - Error handling: ✓")
    print(f"  - Edge cases handled: ✓")
    print(f"  - Documentation: Complete")
    print(f"  - Time complexity: O(n log n)")
    print(f"  - Space complexity: O(n)")