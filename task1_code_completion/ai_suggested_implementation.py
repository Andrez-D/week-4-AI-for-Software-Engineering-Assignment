"""
Task 1: AI-Powered Code Completion - AI-Suggested Implementation
This code represents what an AI tool like GitHub Copilot would suggest
Author: [Kipruto Andrew Kipngetich]
Date: October 2025

NOTE: This is a simulation of AI-generated code based on typical Copilot behavior
"""

# AI Suggestion 1: Simple one-liner (most common Copilot suggestion)
def sort_dict_list_ai_v1(data_list, sort_key, reverse=False):
    """Sort list of dictionaries by specific key."""
    return sorted(data_list, key=lambda x: x[sort_key], reverse=reverse)


# AI Suggestion 2: With error handling (prompted by context)
def sort_dict_list_ai_v2(data_list, sort_key, reverse=False):
    """
    Sort list of dictionaries by specific key with error handling.
    
    Args:
        data_list: List of dictionaries
        sort_key: Key to sort by
        reverse: Sort in descending order if True
        
    Returns:
        Sorted list of dictionaries
    """
    if not data_list:
        return []
    
    try:
        return sorted(data_list, key=lambda x: x[sort_key], reverse=reverse)
    except KeyError:
        # Handle missing keys by using get() with None as default
        return sorted(data_list, key=lambda x: x.get(sort_key), reverse=reverse)


# AI Suggestion 3: More robust version (if you comment "handle missing keys")
def sort_dict_list_ai_v3(data_list, sort_key, reverse=False, default=None):
    """Sort list of dicts by key, handling missing keys with default value."""
    return sorted(data_list, key=lambda x: x.get(sort_key, default), reverse=reverse)


# AI Suggestion 4: Using operator module (more "Pythonic" suggestion)
from operator import itemgetter

def sort_dict_list_ai_v4(data_list, sort_key, reverse=False):
    """Sort list of dictionaries using itemgetter for better performance."""
    return sorted(data_list, key=itemgetter(sort_key), reverse=reverse)


# AI Suggestion 5: In-place sorting (if you mention "modify original")
def sort_dict_list_ai_v5(data_list, sort_key, reverse=False):
    """Sort list in-place to save memory."""
    data_list.sort(key=lambda x: x[sort_key], reverse=reverse)
    return data_list


# ============================================================================
# COMPARISON AND TESTING
# ============================================================================

if __name__ == "__main__":
    import time
    import random
    
    print("="*80)
    print("TASK 1: AI-SUGGESTED IMPLEMENTATION - CODE COMPLETION")
    print("="*80)
    
    # Prepare test data
    test_data = [
        {"name": "Alice", "age": 30, "salary": 75000},
        {"name": "Charlie", "age": 25, "salary": 60000},
        {"name": "Bob", "age": 35, "salary": 85000},
        {"name": "Diana", "age": 28, "salary": 70000}
    ]
    
    # Test all AI versions
    print("\n[Comparison] Testing all AI-suggested versions:")
    print("-" * 80)
    
    print("\n1. AI Version 1 (Simple one-liner):")
    result_v1 = sort_dict_list_ai_v1(test_data, 'salary', reverse=True)
    for emp in result_v1:
        print(f"  {emp['name']}: ${emp['salary']:,}")
    
    print("\n2. AI Version 2 (With error handling):")
    result_v2 = sort_dict_list_ai_v2(test_data, 'salary', reverse=True)
    for emp in result_v2:
        print(f"  {emp['name']}: ${emp['salary']:,}")
    
    print("\n3. AI Version 3 (Handle missing keys):")
    # Test with data that has missing keys
    test_data_missing = test_data.copy()
    test_data_missing.append({"name": "Eve", "age": 32})  # Missing salary
    result_v3 = sort_dict_list_ai_v3(test_data_missing, 'salary', reverse=True, default=0)
    for emp in result_v3:
        salary = emp.get('salary', 'N/A')
        print(f"  {emp['name']}: {salary}")
    
    print("\n4. AI Version 4 (Using itemgetter):")
    result_v4 = sort_dict_list_ai_v4(test_data, 'salary', reverse=True)
    for emp in result_v4:
        print(f"  {emp['name']}: ${emp['salary']:,}")
    
    print("\n5. AI Version 5 (In-place sorting):")
    test_data_copy = test_data.copy()
    result_v5 = sort_dict_list_ai_v5(test_data_copy, 'salary', reverse=True)
    for emp in result_v5:
        print(f"  {emp['name']}: ${emp['salary']:,}")
    
    # Performance comparison
    print("\n" + "="*80)
    print("AI-SUGGESTED IMPLEMENTATION COMPLETE")
    print("="*80)
    
    print("\n💡 TYPICAL AI CODE GENERATION BEHAVIOR:")
    print("  1. Suggests simplest solution first (v1)")
    print("  2. Adds complexity based on context/comments (v2, v3)")
    print("  3. May suggest multiple alternatives")
    print("  4. Often includes 'Pythonic' idioms (itemgetter)")
    print("  5. Tends toward concise over verbose")
    
    print("\n✅ STRENGTHS OF AI-GENERATED CODE:")
    print("  - Very fast to write (seconds vs minutes)")
    print("  - Follows common patterns and idioms")
    print("  - Often syntactically correct")
    print("  - Good for boilerplate code")
    print("  - Suggests modern Python features")
    
    print("\n⚠️  WEAKNESSES OF AI-GENERATED CODE:")
    print("  - May lack comprehensive error handling")
    print("  - Doesn't always consider edge cases")
    print("  - May miss project-specific requirements")
    print("  - Can suggest inefficient solutions for large scale")
    print("  - Requires human review and testing")*80
    print("PERFORMANCE COMPARISON")
    print("="*80)
    
    # Generate large dataset for benchmarking
    large_data = [
        {
            "id": i,
            "value": random.randint(1, 100000),
            "category": random.choice(['A', 'B', 'C'])
        }
        for i in range(50000)
    ]
    
    print(f"\nDataset size: {len(large_data):,} items")
    print("\nBenchmarking each implementation:\n")
    
    implementations = [
        ("AI v1 (Simple)", sort_dict_list_ai_v1),
        ("AI v2 (Error handling)", sort_dict_list_ai_v2),
        ("AI v3 (Default values)", sort_dict_list_ai_v3),
        ("AI v4 (itemgetter)", sort_dict_list_ai_v4),
        ("AI v5 (In-place)", sort_dict_list_ai_v5)
    ]
    
    results = []
    
    for name, func in implementations:
        # Create fresh copy for each test
        test_copy = large_data.copy()
        
        start_time = time.perf_counter()
        
        if name == "AI v3 (Default values)":
            sorted_result = func(test_copy, 'value', default=0)
        else:
            sorted_result = func(test_copy, 'value')
        
        end_time = time.perf_counter()
        
        execution_time = (end_time - start_time) * 1000  # Convert to ms
        results.append((name, execution_time))
        
        print(f"{name:30s}: {execution_time:8.2f} ms")
    
    # Find fastest implementation
    fastest = min(results, key=lambda x: x[1])
    print(f"\n🏆 Fastest: {fastest[0]} ({fastest[1]:.2f} ms)")
    
    # Memory usage comparison
    print("\n" + "="*80)
    print("MEMORY COMPARISON")
    print("="*80)
    
    import sys
    
    small_data = test_data.copy()
    
    print("\nMemory usage (approximate):\n")
    
    # V1-V4 create new lists
    result_new = sort_dict_list_ai_v1(small_data, 'salary')
    mem_new = sys.getsizeof(result_new)
    print(f"New list (v1-v4): {mem_new} bytes")
    
    # V5 modifies in place
    test_inplace = small_data.copy()
    result_inplace = sort_dict_list_ai_v5(test_inplace, 'salary')
    mem_inplace = sys.getsizeof(result_inplace)
    print(f"In-place (v5):    {mem_inplace} bytes")
    print(f"\nDifference: {mem_new - mem_inplace} bytes")
    print("Note: In-place sorting doesn't create a new list, saving memory")
    
    # Code characteristics
    print("\n" + "="*80)
    print("CODE CHARACTERISTICS")
    print("="*80)
    
    print("\n📏 Lines of Code:")
    print(f"  AI v1: 2 lines (1 return statement)")
    print(f"  AI v2: 9 lines (with error handling)")
    print(f"  AI v3: 2 lines (with default parameter)")
    print(f"  AI v4: 3 lines (import + function)")
    print(f"  AI v5: 3 lines (in-place modification)")
    
    print("\n🎯 Code Complexity:")
    print(f"  AI v1: Very Low   - Simple and direct")
    print(f"  AI v2: Medium     - Try-except adds complexity")
    print(f"  AI v3: Low        - Simple with extra parameter")
    print(f"  AI v4: Low        - Uses stdlib, slightly more advanced")
    print(f"  AI v5: Low        - Simple but modifies original")
    
    print("\n✨ Code Quality:")
    print(f"  AI v1: Good       - Works for basic cases")
    print(f"  AI v2: Better     - Handles errors")
    print(f"  AI v3: Best       - Flexible and safe")
    print(f"  AI v4: Good       - Slightly faster, less flexible")
    print(f"  AI v5: Good       - Memory efficient but mutates data")
    
    print("\n⚠️  Potential Issues:")
    print(f"  AI v1: No error handling, fails on missing keys")
    print(f"  AI v2: Broad exception handling might hide bugs")
    print(f"  AI v3: None")
    print(f"  AI v4: Fails on missing keys (no .get() support)")
    print(f"  AI v5: Mutates original list (side effects)")
    
    print("\n" + "=")
          


          
