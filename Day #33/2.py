
#--- Methods in Dict-------------------------------------------------------------------

# (google- python dictionary documentation)

ep= {122:45, 123:89, 567:69, 670:69}
ep2={222:87, 676:67}

ep.update(ep2)  # update ep2 in ep1
print(ep)

# ep.clear()
print(ep)
# empt = {} # print empty dict

ep.pop(123)
print(ep)

ep.popitem()
print(ep)   # pops last item 

# del ep2    # to delete a dict
# del ep[123]   #to delete a value in dict

