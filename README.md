# Run

This command runs the program for the with the required sorting algorithms and permutation sets active.

```bash
python3 src/main.py 4,6,8 --mergesort --heapsort --quicksort --shakersort
```

## Command Line Arguments

- The first command line argument is CSV in which each element must be an integer.
- The following arguments may specify any number of sorting algorithms to run. They are run in the order specified. Any number can be specified, and duplicates are allowed. Only the following values are legal.
  - `--mergesort`
  - `--heapsort`
  - `--quicksort`
  - `--shakersort`
- Running with no commandline arguments or with `--help` or `-h` will show a basic help screen.