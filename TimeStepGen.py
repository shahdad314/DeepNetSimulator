##### rsmct shows the number of line/timestep in the output rsm/csv
# ts = [10,10]
def TimeStepGen(ts):
    """
    these values extracted from the Reservoir simulator software and are fixed for this specific software

    :param ts:
    :return:
    """
    ecl_time = [9, 12, 13, 18, 19, 49, 140, 190]
    ecl_tstep = [0, 1, 4, 9.5, 13, 31.5, 40, 95, 121]

    time_count = int(ts[0])
    time_step = int(ts[1])
    tstep = []
    tstep.append(ecl_tstep[0])
    tstep.append(ecl_tstep[1])
    tstep.append(ecl_tstep[2])
    # print tstep
    if time_step > ecl_time[0] and time_step < ecl_time[2]:
        for l in range(time_count):
            s = (l + 1) * time_step
            tstep.append(s)
    elif time_step > ecl_time[1] and time_step < ecl_time[3]:
        tstep.append(ecl_tstep[3])
        for l in range(time_count):
            s = (l + 1) * time_step
            tstep.append(s)

    elif time_step > ecl_time[4] and time_step < ecl_time[5]:
        tstep.append(ecl_tstep[4])
        for l in range(time_count):
            s = (l + 1) * time_step
            tstep.append(s)

    elif time_step > ecl_time[5] and time_step < ecl_time[6]:
        tstep.append(ecl_tstep[4])
        tstep.append(ecl_tstep[5])
        for l in range(time_count):
            s = (l + 1) * time_step
            tstep.append(s)

    elif time_step > ecl_time[6] and time_step < ecl_time[7]:
        tstep.append(ecl_tstep[4])
        tstep.append(ecl_tstep[6])
        tstep.append(ecl_tstep[7])
        for l in range(time_count):
            s = (l + 1) * time_step
            tstep.append(s)

    elif time_step > ecl_time[7]:
        tstep.append(ecl_tstep[4])
        tstep.append(ecl_tstep[6])
        tstep.append(ecl_tstep[8])
        for l in range(time_count):
            s = (l + 1) * time_step
            tstep.append(s)

    return tstep

