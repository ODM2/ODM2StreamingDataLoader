###Tasks needed to be completed for the ODMStreamLoader###

*Jacob*
  - [x] create function 'canIrun' that determines whether the specified timedelta has reached. If so, a run event will occur.
  - [x] datetime converter params: datetimeUTC, offset
  - [x] database connections need to be put into a panel ( PropertyGrid)
  - [ ] Add functions to api: Create & Read (getAll and by code)         
    - [x] method
      - [x] Create
      - [x] getbyID, getbyCode, getAll
    - [x] processing level
      - [x] Create
      - [x] getbyID, getbyCode, getAll
    - [x] variable 
      - [x] Create
      - [x] getbyID, getbyCode, getAll
    - [x] sampling feature # Core #
      - [x] Create
      - [x] getbyID, getbyCode, getAll
    - [x] site  # Sampling Feature Schema #
      - [x] Create
      - [x] getbyID, getbyCode, getAll
    - [ ] Units # core # 
      - [ ] Create
      - [ ] getbyID, getAll
    - [ ] organization
      - [ ] create
      - [ ] getbyId, getbyCode, getall
    - [ ] people
      - [ ] create
      - [ ] getbyId, getbyCode, getall
  ##Unable to find the following...##
    - [ ] deployment Action # core #
      - [ ] Create
      - [ ] !getbyID, !getbyCode, !getAll
    - [ ] timeseries results # results schema #
      - [ ] Create
      - [ ] getbyID, getAll
    - [ ] timeseries result values # results schema #
      - [ ] Create
      - [ ] getbyID, getAll
    - [ ] results # core #
      - [ ] Create
      - [ ] getbyID, getAll
    - [x] sensor mappings (Backburner....)
  - [x] design config file/schema (json)
  - [x] write json reader/writer
    - [x] convert to object (write custom object_pairs_hook)
  - [x] unittest json reader/writer
  
  - [ ] need to write a function to create new datavalue entry in database (workflow for creating a new data value)
  - [ ] write code for loader ( actual steps the loader needs to take to load data )
  
  - [ ] write the gui
  
*Stephanie*   
  - [ ] update class diagram
  
