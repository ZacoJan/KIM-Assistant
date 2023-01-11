import getopt, sys

from AISource import *
from speech import *
from analysis import *
from config import *

FREEQUERYMODE = FREEMODE


def main():
    argumentList = sys.argv[1:]
    
    # Options
    options = "htac:"
    
    # Long options
    long_options = ["Help", "Text", "Audio", "CSV"]
    
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-h", "--Help"):
                print ("Use -h or --Help for this menu\n" 
                        + "Use -t or --Text to add text input and add a query afterwards\n"
                        + "Example: script.py -t 'Who is Albert Einstein?'\n"
                        + "Use -a or --Audio to use audio mode\n"
                        + "Use -c or --CSV to read in a text file with a query on each line with no commas (Not a CSV file, yet)\n"
                )
                
            elif currentArgument in ("-t", "--Text"):
                print ("Running query on inputted text '({})'".format(sys.argv[2]))
                run_kim(False,str(sys.argv[2]).lower())
                
            elif currentArgument in ("-a", "--Audio"):
                print ("Running query on Audio...")
                run_kim(True,"")

            elif currentArgument in ("-c", "--CSV"):
                print ("Running query on text in csv...")
                queries = runCSV(sys.argv[2])
                run_kim(False,queries)

                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))


# Main function
def run_kim(AUDIOINPUT, command):

    # Listen for command
    if AUDIOINPUT:
        while True:
            command = ''
            command = take_command()
            if command != '':
                query(command)

    else:
        if type(command) == list:
            for question in command:
                query(str(question))

        elif type(command) == str:
            query(command)

        else:
            raise ValueError(command)


def query(command):
    if command != '':

        # Checks for pre compiled query responses
        for phrase in COMMONPHRASES:
            if phrase in command:
                response = commonPhrases(command)
        
        #If free mode enabled query wiki
        if FREEQUERYMODE:
            response = wikiQuery(command)
        
        # If in paid mode query open ai api
        else:
            response = generalQuery(command)
        

        # Logging Functions - Change options in config.py
        if CONSOLELOG:
            print(response)

        if AUDIOOUTPUT:
            talk(response)
        
        if SAVEMODE:
            save_response(response)


if __name__ == "__main__":
    main()