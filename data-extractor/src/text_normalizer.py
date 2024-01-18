class TextNormalizer:
    def normalize(self, text):
        if isinstance(text, str):
            return text
        
        normalized_text = ''

        for segment in text:
            if isinstance(segment, str):
                normalized_text += segment
            else:
                normalized_text += segment['text']

        return normalized_text