# This is tutorial about python decorators and its usage called plugins
#
# youtube topic: Geir Arne Hjelle - Plugins: Adding Flexibility to Your Apps - PyCon 2019
# link: https://speakerdeck.com/pycon2019/jes-ford-getting-started-testing-in-data-science
# Author: Geir Arne Hjelle


# Standard library imports
import pathlib

# Third party imports
import click
import pandas as pd
import matplotlib.pyplot as plt
import json

# plotter imports
import readers



def read_data(file_path):
    """Read data and return Pandas DataFrame """
    format = file_path.suffix.lstrip(".")
    return readers.read(format, file_path)

    """
    func = getattr(readers, format) # gets the function object from another function
    return func(file_path) # passes the argument to the retrieved function
    
 
    if format == 'csv':
        return pd.read_csv(file_path)
    elif format == "json":
        json_dict = json.loads(file_path.read_text())
        return pd.DataFrame(json_dict)
    else:
        raise TypeError(f"{format} not supported")

    return pd.read_csv(file_path)
    """

def creat_plot(data):
    """Plot the data input"""
    data.plot()
    plt.show()


@click.command()
@click.argument("file_path") # read data file
def main(file_path):
    """Read data and create a simple plot"""
    file_path = pathlib.Path(file_path)
    print(f"this is the path: {file_path}\n")
    
    data = read_data(file_path)
    creat_plot(data)


if __name__ == "__main__":
    main()
    