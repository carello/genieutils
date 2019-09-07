## pyATS Genie CLI Tools to Create Mocks

### _work in progress... v1.0_

### Overview
Referencing [DEVNET lab](https://github.com/hpreston/netdevops_demos/tree/master/genie-cli-1). The DevNet lab leverages the capabilities of Genie to use a mock device without the need to access physical infrastructure. More information can be found [here.](https://pubhub.devnetcloud.com/media/pyats-packages/docs/unicon/playback/index.html)

The utilities in this repo helps build the mock files

`Genie1.1.py` creates the commands to build the recordings. You'll need to update the __device_list__ in the python file for your topology. You'll also need a base __testbed.yaml__ file. I used VIRL to create my topology. VIRL can auto generate a testbed.yaml file to use. If you don't use VIRL, you'll need to create this testbed. I've provided an example output from VIRL in the `cp-testsbeds` directory.

`create_testbed_mocks-1.2.py` builds the testbeds yaml files after the recordings are built.

### General Procedure
* Build a topology in VIRL
* Run `VIRL auto generate pyats` to create the connectivity testbed yaml file.
* Use Genie `learn all` to create a baseline. You'll then need to make changes to your topology and rerun the learn. See [DEVNET lab](https://github.com/hpreston/netdevops_demos/tree/master/genie-cli-1) to reference on how do to this. 
* Once you're done making changes and completed the learning, you need to start creating your mock devices. Update the `genie1.1.py` script to reference your files. Comments are in the script.
* The genie1.1.py script doesn't actually run the commmands. It creates a text file that you can use to run these manually.
* Next, edit the excel sheet in the `src` directory for your topology; save a `.csv` in MS-DOS format. Edit the `create_testbed_mocks-1.2.py` to point to these files.
* Refer back to the DevNet lab on how to use.

Note: The jinja2 templates are pretty simple and not very robust. I'm sure there's better ways to do this but this was my first attempt using jinja. The templates are build to ouput the proper format including spaces and line returns. If you edit this file, check your yaml output.


