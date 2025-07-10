""" 
Requires: ijson -> pip install ijson
"""

from sklearn.datasets import load_iris
import pandas as pd
import os
import json
import ijson


def iris_to_json(file_path: str):
    # Load the iris dataset from sklearn
    iris = load_iris()

    # Convert the dataset to a list of tuples
    data = [tuple(row) for row in iris.data]

    # Get target names
    target_names = list(iris.target_names)

    # Create a Pandas DataFrame from the list of tuples
    df = pd.DataFrame.from_records(data, columns=iris.feature_names)

    # Add the target index to the DataFrame
    df["target"] = iris.target

    # Dump data to a JSON file
    df.to_json(file_path, orient="records", indent=4)


def create_new_file_name(
    source_file_name, file_extension, prefix="", postfix=""
) -> str:
    # creates a new file name wit the specified attributes
    new_filename = "".join((prefix, source_file_name, postfix, file_extension))
    return new_filename


def get_json_len(full_source_file_path: str) -> int:
    # get the number of items i.e., dictionaries in file
    try:
        if os.path.isfile(full_source_file_path):
            with open(full_source_file_path, "rb") as fh:
                data_gen = ijson.items(fh, "item", use_float=True)
                n = len(list(data_gen))
                del data_gen
            fh.close()
            return n
    except Exception as e:
        print(e)


def nums_generator(start, step=1):
    # similar to python's range() generator
    x = start
    while True:
        yield x
        x += step


def split_json(full_source_file_path: str, chunk_size: int):
    # the main function that splits the large json into smaller files
    # chunck size referrs to how many dictionaries to place in each smaller file

    if os.path.isfile(full_source_file_path):
        # prepare new directory name
        source_file_name, file_extension = os.path.splitext(
            os.path.basename(full_source_file_path)
        )
        source_dir_name = os.path.dirname(full_source_file_path)
        new_source_dir_name = source_dir_name + "_chunked"
        os.makedirs(new_source_dir_name, exist_ok=True)

        # validate that we are working with a JSON file
        if file_extension == ".json":
            # get the number of items i.e., dictionaies
            big_json_size = get_json_len(full_source_file_path)
            print(f"Big json file items count: {big_json_size}")

            if big_json_size > 0:
                counter = 0
                # instantiate file numbering, stepping in chunk_size amounts
                file_start_nums = nums_generator(0, chunk_size)
                # first start index is 0
                file_start = next(file_start_nums)
                # first stop index is 0 + chunk_size
                file_stop = next(file_start_nums)
                # check if stop index is not over the size of the original JSON file
                if file_stop > big_json_size:
                    file_stop = big_json_size

                with open(full_source_file_path, "rb") as fh:
                    # ijson works as a Generator, thus not loading the whole
                    # JSON file in memory. It yields one item (dict) at a time!
                    data_gen = ijson.items(fh, "item", use_float=True)
                    # iterate though the data generator until the end of the file
                    while counter < big_json_size:
                        # build a temporary list of dictionaries for each new chunk
                        temp_data = []
                        # since ijson is a generator, we can iterate through each item,
                        # without loading the whole JSON file in memory.
                        for item in data_gen:
                            temp_data.append(item)
                            # we iterate for every chunk size
                            # i.e., when counter reaches file_stop - 1,
                            # it has iterated through another chunk size
                            if counter == file_stop - 1:
                                # first write the accumulated data to file
                                if file_start == counter:
                                    # i.e., number of items is less than chunk size
                                    # in the original JSON file
                                    postfix = "".join(("_", str(file_start)))
                                else:
                                    # otherwis, we label start and stop counters in file name
                                    postfix = "".join(
                                        ("_", str(file_start), "_", str(counter))
                                    )
                                # create the new chunked file path and name
                                new_file_path = os.path.join(
                                    new_source_dir_name,
                                    create_new_file_name(
                                        source_file_name,
                                        file_extension,
                                        postfix=postfix,
                                    ),
                                )
                                # write the chunked data to the file
                                print(f"writing: {new_file_path}")
                                with open(new_file_path, "w+") as jf:
                                    json.dump(temp_data, jf, indent=2)

                                # yield next number from the generator and reset temp data
                                file_start = file_stop
                                file_stop = next(file_start_nums)
                                temp_data = []
                            # increment counter to move on to next chunk
                            counter += 1
                    if file_start < big_json_size:
                        # if there is only one dictionary in the JSON file
                        # else if there number of items is less than the chunk size
                        if big_json_size - file_start == 1:
                            postfix = "".join(("_", str(file_start)))
                        else:
                            postfix = "".join(
                                ("_", str(file_start), "_", str(big_json_size - 1))
                            )
                        new_file_path = os.path.join(
                            new_source_dir_name,
                            create_new_file_name(
                                source_file_name, file_extension, postfix=postfix
                            ),
                        )
                        print(f"writing: {new_file_path}")
                        with open(new_file_path, "w+") as jf:
                            json.dump(temp_data, jf, indent=2)
                    # clean up memory
                    del data_gen


if __name__ == "__main__":
    # get current working directory
    current_dir = os.getcwd()

    # # for when you want to write the iris data to json
    # iris_to_json(os.path.join(current_dir ,"iris.json"))

    # split the large json file into smaller files of 3 dictionaries each
    split_json(os.path.join(current_dir, "iris.json"), 3)
