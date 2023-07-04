"""
ParamX - Crate a parameters word lists from JS/HTML/... files
"""

from argparse import ArgumentParser
import re
from utils.patterns import all_patterns


class ParamX:
    def __init__(self, arguments):
        self.arguments = arguments
        self.file = arguments.file
        self.regex_patterns = all_patterns
        self.output = self.arguments.output
        self.create_output_file()
        if arguments.regex_patterns:
            self.regex_patterns = arguments.regex_patterns

    def start_paramx(self):
        content = self.get_content_of_input_file()
        all_found_words = []
        for pt in self.regex_patterns:
            compiled_pattern = re.compile(pt)
            matched_items = compiled_pattern.findall(content)
            if matched_items:
                for m in matched_items:
                    tmp = m.strip()
                    if len(tmp) > 16:
                        continue

                    if m not in all_found_words:
                        if ',' in m:
                            all_vars = m.split(',')
                            for av in all_vars:
                                tmp2 = av.strip()
                                if tmp2 not in all_found_words:
                                    all_found_words.append(tmp2)
                                    self.print_output(text=tmp2)
                        else:
                            all_found_words.append(tmp)
                            self.print_output(text=tmp)

    def get_content_of_input_file(self):
        try:
            with open(self.file, 'r') as input_file:
                return input_file.read()

        except Exception as e:
            print('Error occurred in reading input file : ' + str(e))

    def create_output_file(self):
        if self.output:
            try:
                with open(self.output, 'w') as f:
                    return

            except Exception as e:
                print('Error occurred in creating output file : ' + str(e))
                exit(1)

    def print_output(self, text):
        """
        print output and if --output is set, save the output in file
        :param text:
        :return:
        """

        print(text)
        if self.output:
            try:
                with open(self.output, 'a+') as output_file:
                    output_file.write(text + '\n')

            except Exception as e:
                print('Error occurred in writing on output file : ' + str(e))
                exit(1)


class ScriptParser:
    def __init__(self):
        self.parser = ArgumentParser(usage='python3 %(prog)s --help',
                                     allow_abbrev=False, add_help=False)

    def start_parsing(self):
        self.parser.add_argument('--help', '-h', action='store_true')
        self.parser.add_argument('--file')
        self.parser.add_argument('--output')
        self.parser.add_argument('--regex-patterns', nargs='*', default=[])
        self.parser.add_argument('--show-examples', default=False, action='store_true')

    def print_help(self):
        help_text = f''' Usage:  python3 {self.parser.prog} [Input] [Arguments]

    Input Arguments:
      --file              url addresses to download JS files from URL or URLs

    General Arguments:
      --regex-patterns    set regex patterns list to extract parameters

    Output Arguments:
      --output            save output to a file [optional]

    Help:  
      --help              print help message
      --show-examples     print examples message
'''
        print(help_text)

    def show_examples(self):
        examples_text = f''' Examples:
    python3 {self.parser.prog} --file main.js --output main.txt
    python3 {self.parser.prog} --file main.js --regex-patterns PATTERN1 PATTERN2
    '''
        print(examples_text)

    def get_parser(self):
        """
        return parser object
        :return:
        """
        return self.parser

    def check_arguments(self):
        args, unknown = self.parser.parse_known_args()
        if (args.help is not None) and (args.help is True):
            self.print_help()
            exit()

        if args.show_examples is True:
            self.show_examples()
            exit()

        if args.file is not None:

            paramx = ParamX(arguments=args)
            paramx.start_paramx()

        else:
            print('You have to set source!')
            print('--file is mandatory')
            self.parser.print_usage()


if __name__ == '__main__':
    script_parser = ScriptParser()
    script_parser.start_parsing()
    script_parser.check_arguments()
