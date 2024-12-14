def removes_dublicates (text: str) -> str:
    if not text:
        return text
    else: 
        symbols = list(text)
        unique_symbols = [symbols[0]]
        
        for symbol in range(1, len(symbols)):
            current_symbol = symbols[symbol]
            previous_symbol = symbols[symbol -1]

            if current_symbol != previous_symbol:
                unique_symbols.append(current_symbol)
            
        result = ''.join(unique_symbols)    
        return result

if __name__ == '__main__':
    text = str(input('введите строку: '))
    print(removes_dublicates(text))
    