# ODM2 Streaming Data Loader Developer Environment Setup

1. Install pip.
2. install [miniconda](http://repo.continuum.io/miniconda/index.html) using the appropriate setup script.
3. download the list of [requirements](https://github.com/ODM2/ODM2StreamingDataLoader/blob/master/SDLReq.txt)
3. Setup a new conda environment using python 2.7 and wxPython:
    ```sh
    $ conda create --name SDL-env --file SDLReq.txt
    $ source activate SDL-env
    ```
4. Step 3 will take a while, so go get something from the vending machine.
5. Test the new environment by executing the program. 

### Feedback
Comments and concenrns can be posted on our GitHib page: https://github.com/ODM2/ODM2StreamingDataLoader/issues.
