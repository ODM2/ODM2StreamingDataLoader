# ODM2 Streaming Data Loader Developer Environment Setup

1. Install pip.
2. install [miniconda](http://repo.continuum.io/miniconda/index.html) using the appropriate setup script.
3. download the list of [requirements](https://github.com/ODM2/ODM2StreamingDataLoader/blob/master/SDLReq.yml)
4. Setup a new conda environment using python 2.7 :
    ```sh
    $ conda env create -f SDLReq.yml
    $ source activate SDL-env
    ```
5. Step 4 will take a while, so go get something from the vending machine.
6. Test the new environment by executing the program. 

### Feedback
Comments and concenrns can be posted on our GitHib page: https://github.com/ODM2/ODM2StreamingDataLoader/issues.
