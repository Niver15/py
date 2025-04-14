def read_and_modify_file():
    #ask the user for the input file name
    input_filename =input("enter the input file name: ")
    try:
        #Attempt to open the file for reading
        with open(input_filename, 'r')as
        infile:
        #read the file contents
        content=infile.read()
        #modify the content(you can change this modification as needed)
        modified_content=
        content.upper()  #Example modification:convert text to uppercase
        #Ask the user for the output file name
        output_filename=input("enter the output file name: ")

        #write the modified content to the new file
        with open(output_filename, 'w') as 
        outfile:
        outfile.write(modified_content)
        print(f"file has been modified and saved as{output_filename})

        except FileNotFoundError:
            print(f"Error:The file'{input_filename})' does not exist.")
            except IOError:
                print(f"Error:The file'{input_filename}' could not be read.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
#call the function
read_and_modify_file
