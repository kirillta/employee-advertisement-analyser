class TextNormalizer:
    def normalize(self, text: str) -> str:
        if isinstance(text, str):
            return text
        
        normalized_text: str = ''

        for segment in text:
            if isinstance(segment, str):
                normalized_text += segment
            else:
                normalized_text += segment['text']

        return normalized_text