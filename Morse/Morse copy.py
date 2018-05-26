class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".",
                "..-.","--.","....","..",".---",
                "-.-",".-..","--","-.","---",".--.",
                "--.-",".-.","...","-","..-","...-",
                ".--","-..-","-.--","--.."]
        representations = set()
        for word in words:
            morseCode = ""
            for char in word:
                morseCode += code[ord(char)-97]
            representations.add(morseCode)

        return len(representations)
