class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []

        for ch in first:
            start = first[ch]
            end = last[ch]
            is_valid = True
            
            i = start
            while i <= end:
                if first[s[i]] < start:
                    is_valid = False
                    break
                end = max(end, last[s[i]])
                i += 1
                
            if is_valid:
                valid_intervals.append((start, end))

        valid_intervals.sort(key=lambda x: x[1])
        
        selected_ends = set()
        prev_end = -1
        for start, end in valid_intervals:
            if start > prev_end:
                selected_ends.add(end)
                prev_end = end

        result = []
        for ch in first:
            start = first[ch]
            end = last[ch]
            i = start
            is_valid = True
            while i <= end:
                if first[s[i]] < start:
                    is_valid = False
                    break
                end = max(end, last[s[i]])
                i += 1
            if is_valid and end in selected_ends:
                result.append(s[start:end + 1])

        return result