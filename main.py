class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle edge case for 0
        if numerator == 0:
            return "0"
        
        # Determine the sign
        negative = (numerator < 0) != (denominator < 0)
        
        # Work with absolute values to avoid negative signs
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Calculate integral part
        integral_part = numerator // denominator
        remainder = numerator % denominator
        
        # Prepare the result
        result = "-" if negative else ""
        result += str(integral_part)
        
        # If there's no remainder, return the result
        if remainder == 0:
            return result
        
        result += "."
        
        # Dictionary to store the position of each remainder
        remainder_map = {}
        decimal_part = ""
        
        while remainder != 0:
            # Check if the remainder has been seen before
            if remainder in remainder_map:
                # We found a repeating part
                repeat_index = remainder_map[remainder]
                decimal_part = decimal_part[:repeat_index] + "(" + decimal_part[repeat_index:] + ")"
                break
            
            # Store the position of the current remainder
            remainder_map[remainder] = len(decimal_part)
            
            # Update the remainder for the next digit
            remainder *= 10
            decimal_part += str(remainder // denominator)
            remainder %= denominator
        
        result += decimal_part
        return result

# Example usage:
# sol = Solution()
# print(sol.fractionToDecimal(1, 2))       # Output: "0.5"
# print(sol.fractionToDecimal(2, 1))       # Output: "2"
# print(sol.fractionToDecimal(4, 333))     # Output: "0.(012)"

