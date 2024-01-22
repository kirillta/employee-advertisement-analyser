class TextNormalizer:
    @staticmethod
    def normalize(text: str) -> str:
        if isinstance(text, str):
            return TextNormalizer._remove_stop_symbols(text)
        
        normalized_text: str = ''

        for segment in text:
            if isinstance(segment, str):
                normalized_text += segment
            else:
                normalized_text += segment['text']

        return TextNormalizer._remove_stop_symbols(normalized_text)
    

    @staticmethod
    def _remove_stop_symbols(text: set) -> str:
        return text.replace('\n', '. ') \
            .replace('  ', ' ') \
            .replace(' .', '.') \
            .replace('...', '.') \
            .replace('..', '.') \
            .replace(':.', ':')