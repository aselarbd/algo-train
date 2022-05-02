"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
"""


class Solution(object):

    @staticmethod
    def compress(chars):

        chars.sort()
        char_hash_map = {}
        compress = []

        # Analyse the character array
        for character in chars:
            if character in char_hash_map:
                char_hash_map[character] = char_hash_map[character] + 1
            else:
                char_hash_map[character] = 1

        # Compress the character array
        for key in char_hash_map.keys():
            compress.append(key)
            if char_hash_map[key] > 1:
                compress.append(str(char_hash_map[key]))

        return compress


if __name__ == "__main__":
    print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
    # ['a', '2', 'b', 'c', '3']
