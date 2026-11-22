class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            letters = 0

            while j < n and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            gaps = j - i - 1

            if j == n or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - letters
                space_each = spaces // gaps
                extra = spaces % gaps

                line = ""
                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (space_each + (1 if k - i < extra else 0))
                line += words[j - 1]

            res.append(line)
            i = j

        return res