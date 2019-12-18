import sys #  Import from system
script, input_encoding, error = sys.argv  # python_script utf-8 strict


def main(language_file, encoding, errors):  # creating a mini-script
    line = language_file.readline()  # when "main" is called read this line by line in the file

    if line:  # 總之- as long as their is a line in the file to read this code will run else it will end
        print_line(line, encoding, errors)
        # return main(language_file, encoding, errors)
# calling main again on line 10 simply jumps back to the top to read another line. without it, then
# it would read only read one line. This continues there is no more lines to read.
def print_line(line, encoding, errors):  # this is where the actual encoding happens
    next_lang = line.strip()  # strip removes characters from both left and right
    raw_bytes = next_lang.encode(encoding, errors=errors)  # encode the raw bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)  # # Decode into a string

    print(raw_bytes, "<===>", cooked_string)  # now you have both the unicoded and utf-8


languages = open("languages.txt", encoding="utf-8")  # with all the functions named
# time to open language.txt with utf-8
main(languages, input_encoding, error)  # these are the variables used in mini-script "main"
