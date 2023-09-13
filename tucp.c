#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

// function to copy a single file
void copy_file(const char *src, const char *dest) { // params: pointers to source and destination files
    int sourceFile, destFile; // file descriptors
    char buffer[1024]; // read and write size
    ssize_t bytes;

    // open source file
    if ((sourceFile = open(src, O_RDONLY)) == -1) { // open the source file in read only mode 
        perror("open");
        exit(1);
    }

    // open or create the destination file
    // if source file was opened sucessfully we open the desination file 
    // we can read, write, and create a file
    // if the file already exists it is truncated   
    // we also give the correct permission in the next line 
    // read permission and write permission 
    if ((destFile = open(dest, O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR)) == -1) {
        perror("open");
        exit(1);
    }

    // read from source and write to destination
    // done in chunks of 1024
    while ((bytes = read(sourceFile, buffer, sizeof(buffer))) > 0) {
        write(destFile, buffer, bytes);
    }

    // close source and destination files
    close(sourceFile);
    close(destFile);
}

int main(int argc, char *argv[]) {
    struct stat file; // holds the info about file attributes 

    // Check for minimum number of arguments
    if (argc < 3) {
        printf("Usage: ./tucp Sourcefile Destinationfile OR ./tucp Sourcefile Directory\n");
        exit(1);
    }

    // Determine the type of the destination (file or directory)
    // stat gets information about the named file (uses the path) and then writes to the destination
    if (stat(argv[argc - 1], &file) == -1) {
        perror("stat");
        exit(1);
    }

    // Single file copy
    // .st_mode returns metadatas (data about data) to determine the file type

    // check if the given file is a file
    if (S_ISREG(file.st_mode) && argc == 3) {
        copy_file(argv[1], argv[2]);
    } 
    // Multiple file copy to a directory
    // next check if it is a directory
    else if (S_ISDIR(file.st_mode)) {
        for (int i = 1; i < argc - 1; ++i) {
            char destinationPath[1024];
            snprintf(destinationPath, sizeof(destinationPath), "%s/%s", argv[argc - 1], argv[i]); // take in the destination directory and src file name 
            copy_file(argv[i], destinationPath);                                            // and formats them into a single string (stored in destPath)
        }
    } else {
        printf("Invalid arguments.\n");
        exit(1);
    }

    return 0;
}