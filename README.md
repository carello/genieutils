## pyATS/Genie CLI Tools to Help Create Mock Devices

### v1.0


### Overview

Genie provides a very powerful ability to create mock devices so that you can run test without physical infrastructure. Quite often there's a lot of files that are generated during the mock creation process. The utilities in this repo helps build the mock files.

Referencing [DEVNET lab](https://github.com/hpreston/netdevops_demos/tree/master/genie-cli-1). The DevNet lab leverages the capabilities of Genie to use a mock device without the need to access physical infrastructure. More information can be found [here.](https://pubhub.devnetcloud.com/media/pyats-packages/docs/unicon/playback/index.html)



`Genie1.1.py` creates the commands to build the recordings. You'll need to update the __device_list__ in the python file for your topology. You'll also need a base __testbed.yaml__ file. I used VIRL to create my topology. VIRL can auto generate a testbed.yaml file; running `virl generate pyats`. If you don't use VIRL, you'll need to create this testbed. I've provided an example output from VIRL in the `cp-testbeds` directory.

The script `create_testbed_mocks-1.2.py` builds the testbeds yaml files after the recordings are built that you can use for your mocked environment.

For reference the `outputs` directory holds samples from the script outputs.

### Requirements
	
* Python 3
* I suggest (as a best practice) running in a virtual environment.
* run `pip install -r requirements.txt`


### General Procedure
* Build a topology in VIRL
* Run `virl auto generate pyats` to create the connectivity testbed yaml file.
* Use Genie `learn all` to create a baseline. You'll then need to make changes to your topology and rerun `genie learn all`, saving the output to different directories. See [DEVNET lab](https://github.com/hpreston/netdevops_demos/tree/master/genie-cli-1) to reference on how do to this. 
* Once you're done making changes and completed the learning phase, you'll need to start creating your mock devices. Update the `genie1.1.py` script to reference your files. Comments are in the python script indicating the changes that might be required. Please note that the `genie1.1.py` script doesn't actually run the commmands. It creates a text file that you can use to run these manually.
* Next, edit the excel sheet in the `src` directory for your topology; save a `.csv` file in MS-DOS format. Edit the `create_testbed_mocks-1.2.py` to point to these files.
* Refer back to the DevNet lab on how to use.

Note: The jinja2 templates are pretty rudimentary; there's probably better ways to do this... The templates are built to output proper yaml format, including spaces and line returns. If you edit these template files, please check your yaml output.


