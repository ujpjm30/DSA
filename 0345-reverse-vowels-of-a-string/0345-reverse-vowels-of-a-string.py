class Solution:
    def reverseVowels(self, s: str) -> str:
        # 1. 모음들만 순서대로 뽑아서 리스트 만들기
        vowels = [ch for ch in s if ch.lower() in 'aeiou']
        # 2. 그 모음 리스트를 뒤집기
        vowels.reverse()

        result = []
        v_idx = 0  # 뒤집힌 모음을 하나씩 꺼낼 포인터
        
        for ch in s:
            if ch.lower() in 'aeiou':
                # 모음이면 뒤집힌 리스트에서 하나씩 가져옴
                result.append(vowels[v_idx])
                v_idx += 1
            else:
                # 모음이 아니면 원래 글자 그대로 넣음
                result.append(ch)
        
        # 3. 리스트를 다시 문자열로 합치기
        return ''.join(result)
        