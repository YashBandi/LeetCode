class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Position to write compressed characters
        read = 0   # Position to read characters
        
        while read < len(chars):
            char = chars[read]  # Current character
            count = 0  # Count occurrences of the character
            
            # Count consecutive occurrences of chars[read]
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # If count > 1, write the count as characters
            if count > 1:
                for digit in str(count):  # Convert number to string and write each digit
                    chars[write] = digit
                    write += 1
        
        return write  # New length of modified chars list