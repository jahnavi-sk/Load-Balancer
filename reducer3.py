#!/usr/bin/env python3

import sys


prev_client = None
# prev_endpoint = None 
prev_time = None
correct =0
wrong =0
cost_sum =0


for line in sys.stdin:
    line = line.strip()
    words = line.split()
    prediction_status = words[4]
    cost_per = int(words[5])
    curr_client = words[0]
    # curr_endpoint = words[2]
    # curr_time = words[3]

    # if prev_client == curr_client and prev_time == curr_time :
    #     # print("sameeeeee")
    #     continue

    if prev_client and prev_client != curr_client:
        print(f"{prev_client} {final_prediction} {cost_sum}\t")
        # print(f"{prev_client} {correct} {wrong} {cost_sum}")
        
        correct = 0  
        wrong = 0
        cost_sum =0

    if prediction_status == '1':
        correct += 1
    elif prediction_status == '0':
        wrong += 1
    cost_sum += int(cost_per)



    # prev_endpoint = curr_endpoint
    prev_client = curr_client
    # prev_time = curr_time

    numerator = str(correct)
    denominator = str(int(correct) + int(wrong) )
    final_prediction = numerator + "/" + denominator

if prev_client:
    print(f"{prev_client} {final_prediction} {cost_sum}\t")
    