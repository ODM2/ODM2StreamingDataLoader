import os
import csv


class FileSizeReader:
    '''
    A class for dealing with the file that is used to store and update
    the size of each csv file.
    '''

    def __init__(self, data_file):
        self.data_file = data_file

    def getSizeByName(self, csv_file_path):
        '''
        Lookup a given CSV file and return the size.
        If the file is not found, create an entry for it and
        return 0, which is the byte that we will want to begin
        reading from.

        '''
        # Open the data_file to search for the given csv_file_path.
        with open(self.data_file, 'r') as f:
            for line in f:
                file_path = line.split(',')[0]
                
                # If the file is found, then grab the file size
                # and return it.
                if file_path == csv_file_path:
                    file_size = int(line.split(',')[1].rstrip())
                    return file_size
            
        # The file was not found. We need to append it to
        # to the data_file.
        with open(self.data_file, 'a') as f:
            print "New CSV file...Adding to registry: ", csv_file_path
            # Set the file size as 0 (bytes) so that we read it from
            # the beginning.
            f.write(csv_file_path + ',' + '0\n')
            return 0
        # Error, return -1
        return -1


    def setSizeByName(self, csv_file_path):
        '''
        Update data_file with the new size of the given csv_file_path.
        '''
        # Dictionary to store the contents of a file.
        # key, value pairs are mapped to a filename and size in bytes.
        d = {}
        
        # Open data_file and read it into a dictionary.
        with open(self.data_file, 'r') as f:
            reader = csv.reader(f)

            for line in reader:
                if len(line) == 2:
                    d[line[0]] = line[1]
            
            # Set the size of the given csv_file_path.
            d[csv_file_path] = str(os.path.getsize(csv_file_path))
        
        # Open the data_file to write the updated dictionary contents.
        with open(self.data_file, 'wb') as f:
            writer = csv.writer(f)
            for key, value in d.items():
                writer.writerow([key,value])
            
