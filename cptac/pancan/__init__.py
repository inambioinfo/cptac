#   Copyright 2018 Samuel Payne sam_payne@byu.edu
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import pandas as pd

def list_datasets():
    """List all available datasets."""
    col_names = ["Description", "Data reuse status", "Publication link"]
    col_index = pd.Index(data=col_names, name="Dataset name")
    datasets = {
        }
    dataset_df = pd.DataFrame(data=datasets, index=col_index)
    dataset_df = dataset_df.transpose()
    dataset_df.index.name = "" # Giving the index a name, even though it's an emtpy string, causes a space to be printed between the column names and the first row, which improves readability.
    print(f"Available datasets:\n\n{dataset_df}")
