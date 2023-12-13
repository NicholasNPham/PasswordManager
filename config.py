from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    # Create a Parser
    parser = ConfigParser()
    # Read config file
    parser.read(filename)

    # Get Section, Default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not find in the {1} file'.format(section,filename))
    
    return db