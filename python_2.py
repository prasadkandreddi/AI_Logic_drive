def sliding_window(arr,k):
    window_size=sum(arr[:k])
    max_window=window_size
    for i in range(k,len(arr)):
        window_size+=arr[i]-arr[i-k]
        max_window=max(window_size,max_window)
    return  max_window
        