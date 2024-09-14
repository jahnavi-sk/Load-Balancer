#!/usr/bin/env python3

import sys

prev_time = None
# prev_endpoint=None
prev_client = None
client_grp = []
time_arr = [5] * 11
servers_left =3.0


endpoint_val = {
    'user/profile': 1,
    'user/settings': 2,
    'order/history': 3,
    'order/checkout': 4,
    'product/details': 5,
    'product/search': 6,
    'cart/add': 7,
    'cart/remove': 8,
    'payment/submit': 9,
    'support/ticket': 10
}


for line in sys.stdin:
    line = line.strip()
    words = line.split()
    curr_endpoint = words[2]
    curr_time = words[0]
    curr_client = words[3]
    servers_down = words[4]

    # if(prev_endpoint == curr_endpoint):

    if prev_time == curr_time:
        if curr_client not in client_grp:
            client_grp.append(curr_client)
        elif curr_client in client_grp:
            continue
    else:
        client_grp = [curr_client]

    # elif(prev_endpoint!=curr_endpoint):
        # client_grp = [curr_client]

    if servers_down == '3.0' and prev_time != curr_time:
        time_arr = [5] * 11

    if servers_down == '3.0':
        status= '500'


    else:
        servers_left = 3.0 - float(servers_down)-1
        # curr_time = -1
        # print("arr: ", time_arr)
        if prev_time == curr_time:
            remaining = endpoint_val[curr_endpoint]
            # servers_left = '3.0' - servers_down
            # servers_left = 3.0 - float(servers_down) -1
            if time_arr[remaining] == 5:
                time_arr[remaining] = servers_left
                status = '200'
                # print("remaining (5555)= ", time_arr[remaining])
            else:
                # print("remaining before = ", time_arr[remaining])
                if time_arr[remaining] > 0:
                    status ='200'
                    time_arr[endpoint_val[curr_endpoint]] -= 1
                    
                else:
                    status='500'
                # print("remaining = ", time_arr[endpoint_val[curr_endpoint]])

        else:
            status= '200'
            # print ("##################")
            # print ("##################")
            time_arr = [5] * 11
            time_arr[endpoint_val[curr_endpoint]] = servers_left

    # prev_endpoint = curr_endpoint
    prev_time = curr_time
    prev_client = curr_client



    if words[6]== status:
        prediction_status = '1'
    elif words[6]!=status:
        prediction_status = '0'

    if status=='200':
        cost_corr = words[5]
    elif status=='500':
        cost_corr = '0'
    

    print(f"{words[3]} {words[1]} {words[2]} {words[0]} {prediction_status} {cost_corr} {status}")
    # print(line)


    # print (f"{words[2]} {words[0]} {words[1]} {words[3]} {words[4]} {words[5]} {words[6]}")
    # print(client_grp)


# 00:00:46 cart/add r216 c05 2.0 700 200
# 00:00:46 cart/remove r999 c07 3.0 800 200
# 00:00:46 product/search r116 c07 3.0 600 200
# 00:00:46 support/ticket r007 c01 1.0 1000 200
