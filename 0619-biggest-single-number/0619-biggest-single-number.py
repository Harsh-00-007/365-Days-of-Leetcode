import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # Drop numbers that appear more than once
    single_numbers = my_numbers.drop_duplicates(subset=['num'], keep=False)
    
    # Get the maximum single number, or None if empty
    max_num = single_numbers['num'].max() if not single_numbers.empty else None
    
    # Return as DataFrame matching expected schema
    return pd.DataFrame({'num': [max_num]})