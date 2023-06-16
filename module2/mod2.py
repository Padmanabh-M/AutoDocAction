def compute_trend_variable(group):
    """
    Calculates features i.e trend variables for 2,3,5,10 days

    Parameters
    ---------
    group: DataFrame group
        group of ticker_id
    
    Returns
    ------
    df: Dataframe
        dataframe for all features for ticker_ids

    Steps
    -----
    1. Make input array of closing prices
    2. Iterate over number of days(k) to calculate trend variable
        2.1 Append NaN values for first 10 days to temporary array td
        2.2 Iterate from 10th day to avoid undefined values of t10
            2.2.1 Calculate sum of absolute differences of closing prices of consecutive days for past k days
            2.2.2 Divide the absolute difference of closing price of ith day and (i-k)th day by sum and append final value to td araay 
        
    """

    #array of number of days to calculate trend variables
    d = [2,3,5,10]  

    #empty array to store trend variable data
    t = []          

    #Step 1: Input array containing closing price
    cp_data = group['close'] 
    cp_data = cp_data.reset_index(drop=True)

    #Step 2: Iterate over number of days to calculate trend variable
    for k in d:

        #create empty array to store trend variable arrays
        td=[]

        #Step 2.1: Append NaN values for first 10 days
        for i in range(10):
            td.append(np.nan)

        #Step 2.2: Iterate from 10th day to avoid undefined values of t10
        for i in range (10, len(cp_data)):
            #Step 2.2.1: Calculate sum of absolute differences of closing prices of consecutive days for past k days
            sum = 0
            for j in range (i-k, i):
                sum+= abs(cp_data[j+1] - cp_data[j])
            #Step 2.2.2: Divide the absolute difference of closing price of ith day and (i-k)th day by sum and append final value to td araay
            td.append(abs(cp_data[i]-cp_data[i-k])/sum)

        #append the array containing trend variable over past k days to main array
        t.append(td)

    #return dataframe of t2,t3,t5 and t10
    return pd.DataFrame({"t2":t[0], "t3":t[1],"t5":t[2],"t10":t[3] }, index=group.index)
