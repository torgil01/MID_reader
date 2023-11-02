# MID_reader
Read CSV logfiles from MID paradigm and convert to SPM design


## Usage 

```sh
python convert_mid.py -c MID_example.csv -o mid.txt
```

This will read the input file "MID_example.csv" and convert it to a
SPM-type onsets file on the form "id_<id_num>_<datestr>_mid.txt" e.g. 
The ID number and date of the experiment are insered in the filename 

The SPM onsets file is a simple text file with three columns, 
1. the trial number. **Note** This has to match the order of trials in the SPM design (see below) 
2. onset time in seconds (remember to specify timing in sec to SPM)
3. duration of trial in seconds

### Numbering of trial types
```
     1  reward.low
     2  reward.high
     3  neutral
     4  loss.low
     5  loss.high
```

