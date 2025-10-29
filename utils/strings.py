
def is_palindrome(text: str) -> bool:

    cleaned_chars = []
    for ch in text:
        if ch.isalnum():            
            cleaned_chars.append(ch.lower())

    i = 0
    j = len(cleaned_chars) - 1

   
    while i < j:
        if cleaned_chars[i] != cleaned_chars[j]:
            return False
        i += 1
        j -= 1

        return True
 


