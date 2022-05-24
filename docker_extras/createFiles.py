import yaml

def readConfig(configFile):
    """
    It reads a YAML file and returns an object with the data
    
    :param configFile: the path to the config file
    :return: A class object with the attributes of the yaml file.
    """
    with open(configFile) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # transform json into object
    class Struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    returnData = Struct(**data)

    return returnData



def generate_hooks(features):
    """
    It takes a list of features and generates a webhooks.yml file that will pass those features to the
    decide.sh script
    
    :param features: a list of features you want to be able to toggle
    """
    base = """
- id: decide
  execute-command: "/etc/webhook/decide.sh"
  command-working-directory: "/etc/webhook/"
  include-command-output-in-response: true
  pass-arguments-to-command:"""
    for i in features:
        appendment = f'''
  - source: url
    name: {i}'''
        base += appendment
    with open('docker_extras/hooks.yml', 'w+')as f:
        f.write(base)

def generate_decideSH(features):
    """
    It takes a list of features and returns a string that can be used as a shell script to generate a
    new csv file with the features in the list.
    
    :param features: list of features
    """

    # Setup the base variables
    base = "#!/bin/sh\n"
    printline = 'printf "'
    ss = ""
    variables = ""
    counter = 1

    # Dynamically create the shell variables
    # var=$1
    for i in features:
        base += f'{i}=${counter}\n'
        counter += 1
    
    # Dynamically build the printf statement which will write the csv
    for i in features:
        printline += f'{i},'
        ss += r"%s,"
        variables += f'''"${i}" '''

    # Compose the printf statement
    # printf "var\n%s" "$var" > /app/data/new.csv
    printline = printline[:-1] + r"\n" + ss[:-1] + '" ' + variables + "> /app/data/new.csv"

    # Write the decide.sh file
    with open('docker_extras/decide.sh', 'w+')as f:
        f.write(base)
        f.write('\n')
        f.write(printline)
        f.write('\n')
        f.write("sleep 0.2;cat /app/data/result.txt;rm /app/data/result.txt")

    
data = readConfig("data/config.yml")

features = data.data["features"]

generate_hooks(features)
generate_decideSH(features)
