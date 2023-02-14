def read_sites_info(filename):
    "reads files reurns dictionary"
    infile=open(filename)
    location=infile.read()
    infile.close()
    location= location.splitlines()
    location=location[1:]
    site_data={}
    for i in location:
        number,address,city = i.split(",")
        site_data[int(number)]=(address,city)    
    return site_data

def limited_string(s,max_len):
    "max length"
    if len(s) > max_len:
        return s[0:max_len-3]+"..."
    else:
        return s
   
def print_sites_table(sites_info):
    "prints a table"
    print("Site table\n==========")
    print(f'{"ID":>8}:  {"Name":<45}{"Region":<20}')
    for site_id, data in sorted(sites_info.items()):
        limited_name=limited_string(data[0],40)
        region=data[1]
        print(f'{site_id:8}:  {limited_name:45}{region:20}')
       
def get_valid_site_id(sites_info):
    "gets input of site id"
    finish = False
    
    while not finish:
        site_id_input= input("Enter a site id number (? for help): ")
        
        if site_id_input == "?":
            print_sites_table(sites_info)
        
        try:
            int_id = int(site_id_input)
        except ValueError:
            print("You must enter a valid integer")
        
        else:
            
            if int(site_id_input) in sites_info:
                finish = True
            
            else:
                print("Unknown site number")            
     
    return int(site_id_input)

sites = {
    23: ("Hamilton", "Waikato"),
    87: ("Dunedin", "Otago"),
    36: ("Tauranga", "Bay of Plenty")
}
print(get_valid_site_id(sites))
