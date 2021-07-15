save_file = open("example_saves/451.2.2_bosporan_kingdom.rome", 'r')

def clean_port_ids(port_list):
        if port_list.isnumeric(): return True
        else: return False

def return_ports(nation, nation_tag):
    flag = 0
    index = 0
    
    for line in save_file:
        index += 1
        
        if nation_tag in line:
            flag = 1
            save_nation_line = index
            print(save_nation_line)

        if flag == 1 and "ports={" in line:
            save_ports_line = index
            print(save_ports_line)
            ports = line.split()
            clean_ports = list(filter(clean_port_ids, ports))
            print("\n", clean_ports)

            save_file.close()
            break

    if flag == 0:
        print('\nTag for', nation, 'not found')
    else:
        print('\nTag for', nation, 'found in line:', save_nation_line)

    save_file.close()