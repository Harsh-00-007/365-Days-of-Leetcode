class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # Store elements of list1 and their indices in a dictionary
        restaurant_map = {restaurant: i for i, restaurant in enumerate(list1)}
        
        min_sum = float('inf')
        result = []
        
        # Iterate through list2 to find matches and check index sums
        for j, restaurant in enumerate(list2):
            if restaurant in restaurant_map:
                current_sum = j + restaurant_map[restaurant]
                
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [restaurant]  # Found a new strictly smaller sum, reset list
                elif current_sum == min_sum:
                    result.append(restaurant)  # Found another restaurant with the same minimum sum
                    
        return result