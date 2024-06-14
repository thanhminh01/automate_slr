Project Setup Guide
Prerequisites
Ensure you have the following installed:

Python (version 3.x)
Anaconda (or Miniconda)

Setup Instructions

Step 1: Create the Conda Environment
Open a terminal or Anaconda Prompt.

Navigate to the directory containing the sample_env.yml file.

Run the following command to create the environment:

> conda env create -f sample_env.yml --name sample_env

Step 2: Create a Jupyter Notebook Kernel
Activate the newly created environment:

> conda activate sample_env
Install the Jupyter kernel:

> python -m ipykernel install --user --name sample_env --display-name "sample_env"

Step 3: Launch Jupyter Notebook
Deactivate any currently active conda environment:

> conda deactivate
Reactivate the sample_env environment:

> conda activate sample_env
Start Jupyter Notebook:

jupyter notebook

Step 4: Open the Notebook
In the Jupyter interface, navigate to and open text_extraction.ipynb.
Ensure that the notebook is using the sample_env kernel by selecting it from the kernel options.

-------------------------------------------------
pdf_text_extraction.ipynb

Cell 1: Set up the environment with your GPT-4 API key and specify the path to the PDF folder.

Cell 2: Create a list of `Dokument` objects for storing DOIs and raw text extracted from the documents.

Cell 3 (optional): Print a debug message showing the number of documents processed.

Cell 4: Define a function to count the number of tokens in a document and store this information in the object. Print a debug message identifying documents that have raw data exceeding the token limit of your chosen model.

Cell 5: Define the GPT model and run the token counting function. Filter out documents that are too long. Print a message showing the number of documents remaining after the filter.

Cell 6: Use `pickle` to save the list of `Dokument` objects to a file of your choice.

___________________________________________________

11_bias

Cell 1: Set up the environment with GPT4 key

Cell 2: Import necessary modules and load the dokument_list from a pickle file.

Cell 3: Define the template and setup for signalling questions.

Cell 4: Define and execute a function to answer signalling questions for each document.

Cell 5: Define the template and setup for determining overall Risk of Bias (RoB).

Cell 6: Define and execute a function to determine the overall Risk of Bias from signalling question answers.

Cell 7: Save the updated dokument_list using pickle.

Cell 8 (optional): Print the Risk of Bias results for a document of choice.
______________________________________________
13c_visualization

Cell 1 : Set up the environment with your GPT-4 API key

Cell 2: Import necessary modules and load the dokument_list from a pickle file.

Cell 3: Define a template for extracting data from documents and create the extraction processing chain.

Cell 4: Use the extraction chain to process the raw data of the fourth document in the list.

Cell 5: Define a template for generating Python code to visualize extracted data and create the visualization processing chain.

Cell 6: Use the visualization chain to generate Python code for visualizing the extracted data and print the generated code.

Manually take the generated Python code from doklist_3_visualized into a new cell and execute it.

-------------------------------------------------
13a_Eligibility

Cell 1: Set up the environment with your GPT-4 API key and specify the research topoic

Cell 2: Import necessary modules and load the dokument_list from a pickle file.

Cell 3: Define and format a template for a boolean eligibility prompt and create the eligibility boolean processing chain.

Cell 4: Define and format a detailed eligibility template and create the detailed eligibility processing chain.

Cell 5: Define an asynchronous function to evaluate document eligibility, run eligibility checks using GPT-4 model chains, and store eligible documents.

Cell 6: Count and print the number of documents eligible for the chosen research topic.

Cell 7: Save the synthesis_task object containing eligible document information to a pickle file.

______________________________________________
13d_Synthesis

Cell 1: Set up the environment with your GPT-4 API key

Cell 2: Load the synthesis_task object from a pickle file

Cell 3: Define a template for extracting codes from documents and create the coding processing chain.

Cell 4: Define an asynchronous function to assign codes to each document and print the assigned codes.

Cell 5: Define a template for identifying themes from coded data and create the thematic analysis processing chain.

Cell 6: Define an asynchronous function to identify themes from the coded data and print the identified themes.

Cell 7: Prepare the themes output and check if it's token count is within the model's limit.

Cell 8: Define a template for synthesizing overarching themes and create the synthesis processing chain.

Cell 9: Invoke the synthesis chain to generate the final list of overarching themes and print the result.

Cell 10: Save the synthesis result into a new file with "_finished" added to the file name.

**Cell 11 onwards: Optional for viewing results, can be executed seperately from the previous cells.**

Cell 11: Load the final synthesis_task_result object from the pickle file and print the research topic.

Cell 12 (Optional)
Print the codes of a specified document by its index.

Cell 13 (Optional)
Print the themes of a specified document by its index.

Cell 14 (Optional)
Print the synthesis result from processing all eligible documents.