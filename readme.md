Known Information Management (KIM) assistant.

KIM is designed to answer questions by connecting audio / text inputs to multiple data sources such as OpenAI's models, wikipedia and yahoo finance. Can be used as an assistant that can save responses and improve overtime.


Data Sources:
Uses OpenAI's GPT3.5, Codex and Dalle to answer user queries that can be text or audio inputs.
An API key is required which costs money per request to OpenAI. There are free data sources available such as wikipedia and (more coming soon).



USAGE:

Use -h or --Help for the help menu

Use -t or --Text to add text input and add a query afterwards
Example: script.py -t 'Who is Albert Einstein?'

Use -a or --Audio to use audio mode

Use -c or --CSV to read in a text file with a query on each line with no commas (Not a CSV file, yet)
Example: script.py --CSV ListOfQueries.txt


Config:
Edit config.py for spoken responses, saved responses and free / paid mode.