# ODM2 Streaming Data Loader Developer Environment Setup

1. Install pip.
2. install [miniconda](http://repo.continuum.io/miniconda/index.html) using the appropriate setup script.
3. Setup a new conda environment using python 2.7 and wxPython:
    ```sh
    $ conda create -n SDL-env python=2.7 wxpython
    $ source activate SDL-env
    ```
4. In a new conda environment, install the following packages:
    ```sh
    $ pip install numpy pandas pymysql sqlalchemy six pyyaml pytz python-dateutil pytest py geoalchemy2
    ```
5. Step 4 will take a while, so go get something from the vending machine.
6. Test the new environment by executing the program. 

### Feedback
Comments and concenrns can be posted on our GitHib page: https://github.com/ODM2/ODM2StreamingDataLoader/issues.