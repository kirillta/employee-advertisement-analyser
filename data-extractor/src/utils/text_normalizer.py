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
        t1 = text.replace('\n', '. ')
        t2 = t1.replace('  ', ' ')
        t3 = t2.replace(' .', '.')
        t4 = t3.replace('...', '.')
        t5 = t4.replace('..', '.')
        t6 = t5.replace(':.', ':')

        return t6