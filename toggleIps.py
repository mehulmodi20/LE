
def update_state_and_caluate_impact(existing_state, indexes_to_update):
    updated_state = existing_state.copy()
    impact = 0
    for c in indexes_to_update:
        prev_state = updated_state[c]
        new_state = prev_state
        if prev_state <= 0.5:
            new_state += 0.5
        elif prev_state == 1:
            new_state -= 0.5
        updated_state[c] = new_state
        if (existing_state[c] < 1 and updated_state[c] == 1) or (existing_state[c] == 1 and updated_state[c] < 1):
            impact += 1

    return (updated_state, impact)


def build_device_map(connections):
    devices = dict()
    for index, conn in enumerate(connections):
        conni = devices.get(conn[0], [])
        conni.append(index)
        devices[conn[0]] = conni
        conni = devices.get(conn[1], [])
        conni.append(index)
        devices[conn[1]] = conni
    return devices.copy()


def numberOfDevices(connections, toggleIps):
    impact_count = [0]*len(toggleIps)
    # initially all connections are inactive
    connection_state = [0]*len(connections)
    devices = build_device_map(connections)
    print(devices)
    print(toggleIps)
    last_update = dict()
    for index, ip in enumerate(toggleIps):
        prev_connection_state = connection_state.copy()
        print(prev_connection_state)
        print(ip)
        impact = 0
        conns = devices.get(ip, None)
        # if no such IP is present in connections
        if conns is None:
            impact_count[index] = 0
            continue
        for c in conns:
            if not last_update.get(c, 0):
                last_update[c] = ip
            else:
                if last_update[c] == ip and prev_connection_state[c] == 0.5:
                    print(
                        f"removing {ip} since it already updated connection {c}")
                    conns.remove(c)
                last_update[c] = ip
        (new_connection_state, impact) = update_state_and_caluate_impact(
            prev_connection_state, conns)
        print(new_connection_state)
        impact_count[index] += impact
        connection_state = new_connection_state.copy()

    return impact_count


if __name__ == '__main__':
    result = numberOfDevices([["192.167.0.0", "192.167.0.1"],
                              ["192.167.0.2", "192.167.0.0"],
                              ["192.167.0.0", "192.167.0.3"]],

                             ["192.167.0.1",
                              "192.167.0.0",
                              "192.167.0.2",
                              "192.167.0.0",
                              "0.0.0.0"])
    print(result)
